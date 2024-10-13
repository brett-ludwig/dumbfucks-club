provider "google" {
  project = var.project
  region  = "us-west1"
}

resource "google_compute_project_default_network_tier" "project-tier" {
  network_tier = "STANDARD"
}

data "google_compute_subnetwork" "dumbfucks_subnet" {
  name = "dumbfucks-subnet"
  region = "us-west1"
}

# Create a single Compute Engine instance
resource "google_compute_instance" "bookstack-vm" {
  name         = "bookstack-vm"
  machine_type = "e2-small"
  zone         = "us-west1-a"
  tags         = ["ssh", "external", "personal-site"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size = 20
    }
  }
  
  network_interface {
    subnetwork = data.google_compute_subnetwork.dumbfucks_subnet.id
  }
  
  scheduling {
    preemptible         = true
    provisioning_model  = "SPOT"
    automatic_restart   = false
    instance_termination_action = "STOP"
  }
}
