provider "google" {
  project = var.project
  region  = "us-west1"
}

resource "google_compute_project_default_network_tier" "project-tier" {
  network_tier = "STANDARD"
}

resource "google_app_engine_application" "personal-website-engine-app" {
  project     = var.project_name
  location_id = "us-west1"
}

resource "google_storage_bucket" "app" {
  name          = "${var.project}-${random_id.app.hex}"
  location      = "US"
  force_destroy = true
  versioning {
    enabled = true
  }
}

resource "random_id" "app" {
  byte_length = 8
}

data "archive_file" "function_dist" {
  type        = "zip"
  source_dir  = "../service"
  output_path = "../target/app.zip"
}

resource "google_storage_bucket_object" "app" {
  name   = "app.zip"
  source = data.archive_file.function_dist.output_path
  bucket = google_storage_bucket.app.name
}

resource "google_app_engine_application_url_dispatch_rules" "personal-website-app-dispatch-rules" {
  dispatch_rules {
    domain = "*"
    path = "/*"
    service = "default"
  }
}

resource "google_app_engine_standard_app_version" "latest_version" {

  version_id = var.deployment_version
  service    = "default"
  runtime    = "python310"

  entrypoint {
    shell = "fastapi run app.py --port 8000"
  }

  deployment {
    zip {
      source_url = "https://storage.googleapis.com/${google_storage_bucket.app.name}/${google_storage_bucket_object.app.name}"
    }
  }
  
  

  instance_class = "F1"

  automatic_scaling {
    max_concurrent_requests = 10
    min_idle_instances      = 1
    max_idle_instances      = 3
    min_pending_latency     = "1s"
    max_pending_latency     = "5s"
    standard_scheduler_settings {
      target_cpu_utilization        = 0.5
      target_throughput_utilization = 0.75
      min_instances                 = 0
      max_instances                 = 4
    }
  }
  noop_on_destroy = true
  delete_service_on_destroy = true
}
