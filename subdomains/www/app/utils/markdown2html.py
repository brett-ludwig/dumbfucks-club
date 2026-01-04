import re
from fastapi import  Request


request_ref: Request = None

# the following function can produce the following tailwind classes. They are listed so tailwind cli generates them in css code
# text-xl, text-2xl, text-3xl, text-4xl, text-5xl, text-6xl
def headers(match: re.Match):
    header_class = ""
    # header 6 is meant to be small, but text-6xl is 6 time larger than text-xl. This resolve that
    header_value = 4 - len(match.group(1))
    header_content = match.group(2).strip()
    match header_value:
        case 1:
            header_class = "text-xl"
        case value if value <= 6:
            header_class = f"text-{value}xl"
        case _:
            header_class = "text-xl"
            
    return f'<h{header_value} class="{header_class}">{header_content}</h{header_value}>'

def horizontal_lines(match: re.Match):
    return "<hr>"

def table_heads(match: re.Match):
    return f'<th class="text-center">{match.group(1).strip()}</th>'

def table_items(match: re.Match):
    return f'<td class="p-1">{match.group(1).strip()}</td>'

def data_row(match: re.Match):
    row = match.group(1)
    row = minor_transformations["table_item_prog"].sub(table_items, row)
    return f'<tr>{row}</tr>'

def data_rows(match: re.Match):
    table_data = match.group(1)
    table_data = minor_transformations["table_rows_prog"].sub( data_row, table_data)

    return f"<tdata>{table_data}</tdata>"

def header_row(match: re.Match):
    row = match.group(1)
    row = minor_transformations["table_item_prog"].sub(table_heads, row)
    return f'<thead class="bg-slate-200 py-2"><tr>{row}</tr></thead>'


def table_greedy(match: re.Match):
    table = f'</pre><table class="table-auto text-left text-sm/6">\n{match.group(1)}\n</table><pre class="text-wrap">'
    table = minor_transformations["table_rows_prog"].sub( header_row, table, count=1)
    table = minor_transformations["waste_rows_prog"].sub( "", table)
    table = minor_transformations["table_greedy"].sub( data_rows, table)

    return table

def hyperlinks(match: re.Match):
    return f'<a href="/blogs/{match.group(1)}" class="hover:underline text-blue-600">{match.group(0)}</a>'

def images(match: re.Match):
    return f'<img alt="{match.group(1)}" src="{ request_ref.url_for('static', path=f'assets/img/{match.group(1)}')}" class="mx-auto"></img>'

def external_links(match: re.Match):
    return f'<a rel="noopener noreferrer" target="_blank" href="{match.group(0)}" class="hover:underline text-blue-600">{match.group(0)}</a>'

def numbered_list(match: re.Match):
    whole_list = match.group(0)
    list_item_iter = minor_transformations["numbered_list_item"].finditer(whole_list)
    nested_level = 0
    list_html = '</pre><ol class="list-decimal list-inside">\n'
    for item in list_item_iter:
        new_nested_level = len(item.group(1))
        list_item_content = item.group(2)
        padding_class = ""
        # for tailwind generation: ml-4 ml-8 ml-12 ml-16 ml-20
        if new_nested_level > 0:
            padding_class = f"ml-{new_nested_level * 4}"

        match new_nested_level - nested_level:
            case 1: # open of new nested list
                list_html = list_html + f'<ol class="list-decimal list-inside">\n<li class="{padding_class}">{list_item_content}</li>\n'
            case -1: # end of nested list
                list_html = list_html + f'<li class="{padding_class}">{list_item_content}</li>\n</ol>\n'
            case 0: # no change in nesting 
                list_html = list_html + f'<li class="{padding_class}">{list_item_content}</li>\n'
            case _: # broken formatting. report format issue but still continue
                print("FORMATTING ERROR IN THE FOLLOWING LIST BLOCK")
                print(whole_list)
                list_html = list_html + f'<li class="{padding_class}">{list_item_content}</li>\n'

        nested_level = new_nested_level
    list_html = list_html + '\n</ol><pre class="text-wrap">'
    return list_html



massive_url_regex = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""

main_transformations = [
    # HEADERS: looks for occurrences of '#' and matches the whole line
    {"program": re.compile(r"(#+)(.*)"), "function":headers},
    # HORIZONTAL LINES: finds horizontal lines
    {"program": re.compile(r"___"), "function": horizontal_lines}, 
    # TABLES: Looks for lines that start and end with | greedily to match whole table
    {"program": re.compile(r"^(\|.*\|)$", re.DOTALL | re.MULTILINE), "function":table_greedy}, 
    {"program": re.compile(massive_url_regex), "function": external_links},
    {"program": re.compile(r"\!\[\[([^\]]*)\]\]?"), "function": images},
    {"program": re.compile(r"\[\[([^\]]*)\]\]?"), "function": hyperlinks},
    # Looks for tabs to account for nested lists and newline at end to capture whole block
    {"program": re.compile(r"^(\t*[0-9]+\..*\n)+", re.MULTILINE), "function": numbered_list},
    # {"program": re.compile(r""), "function": },

]

minor_transformations = {
    # TABLES: main transformation re-used for tdata
    "table_greedy": re.compile(r"^(\|.*\|)$", re.DOTALL | re.MULTILINE),
    # same as table greedy, but without including newline so each row is independent
     "table_rows_prog": re.compile(r"^\|(.*\|)$", re.MULTILINE),
    # match waste row produced by markdown formatting
    "waste_rows_prog" : re.compile(r".*?\-{4,}.*", re.MULTILINE),
    # matches an individual row item by looking for | lazily.
    "table_item_prog" : re.compile(r"(.*?)\|"),
    "numbered_list_item": re.compile(r"(\t*)[0-9]+\.(.*)"),
}


# TODO: look into using an AST for this since this is actual parsing
# TODO: use caching for this to avoid wasted compute
def markdown2html(request, markdown):
    global request_ref
    request_ref = request
    for transformation in main_transformations:
        markdown = transformation["program"].sub( transformation["function"], markdown)
    return markdown