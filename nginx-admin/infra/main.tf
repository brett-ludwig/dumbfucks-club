# --- Shared Setup ---
provider "google" {
  project = var.project
  region  = "us-west1"
}

resource "google_compute_project_default_network_tier" "project-tier" {
  network_tier = "STANDARD"
}

resource "google_compute_network" "dumbfucks_network" {
  name                    = "dumbfucks-network"
  auto_create_subnetworks = false
  mtu                     = 1460
}

resource "google_compute_subnetwork" "dumbfucks_subnet" {
  name          = "dumbfucks-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-west1"
  network       = google_compute_network.dumbfucks_network.id
}

# --- NGINX Adming Setup ---

resource "google_compute_address" "static" {
  name          = "ipv4-address"
  address_type  = "EXTERNAL"
  region         = "us-west1"
  network_tier = "STANDARD"
}

resource "google_compute_firewall" "ssh" {
  name          = "allow-ssh"

  allow {
    ports    = ["22"]
    protocol = "tcp"
  }
  direction           = "INGRESS"
  network             = google_compute_network.dumbfucks_network.id
  priority            = 1000
  source_ranges       = ["0.0.0.0/0"]
  target_tags         = ["ssh"]
}

resource "google_compute_firewall" "personal-site" {
  name          = "personal-site"

  allow {
    ports    = ["8000"]
    protocol = "tcp"
  }
  direction           = "INGRESS"
  network             = google_compute_network.dumbfucks_network.id
  priority            = 1000
  source_ranges       = ["0.0.0.0/0"]
  target_tags         = ["personal-site"]
}

resource "google_compute_firewall" "nginx" {
  name    = "nginx"

  network = google_compute_network.dumbfucks_network.id

  allow {
    protocol = "tcp"
    ports    = ["81"]
  }
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["nginx"]
}

resource "google_compute_firewall" "external" {
  name    = "external"

  network = google_compute_network.dumbfucks_network.id

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["external"]
}


# Create a single Compute Engine instance
resource "google_compute_instance" "nginx-admin" {
  name         = "nginx-vm"
  machine_type = "e2-micro"
  zone         = "us-west1-a"
  tags         = ["external", "nginx"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.dumbfucks_subnet.id

    access_config {
      # Include this section to give the VM an external IP address
      nat_ip = google_compute_address.static.address
    }
  }
}
