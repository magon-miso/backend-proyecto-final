## Application configurations
account      = 101526122836
region       = "us-east-1"
profile      = "default"
app_name     = "abcjobs"
env          = "dev"
app_services = ["candidatos-qry", "pruebas-qry", "preguntas-qry"]

#VPC configurations
cidr               = "10.10.0.0/16"
availability_zones = ["us-east-1a", "us-east-1b"]
public_subnets     = ["10.10.50.0/24", "10.10.51.0/24"]
private_subnets    = ["10.10.0.0/24", "10.10.1.0/24"]

#Internal ALB configurations
internal_alb_config = {
  name      = "Internal-Alb"
  listeners = {
    "HTTP" = {
      listener_port     = 80
      listener_protocol = "HTTP"
    }
  }

  ingress_rules = [
    {
      from_port   = 80
      to_port     = 3000
      protocol    = "tcp"
      cidr_blocks = ["10.10.0.0/16"]
    }
  ]

  egress_rules = [
    {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["10.10.0.0/16"]
    }
  ]
}

#Friendly url name for internal load balancer DNS
internal_url_name = "service.internal"

#Public ALB configurations
public_alb_config = {
  name      = "Public-Alb"
  listeners = {
    "HTTP" = {
      listener_port     = 80
      listener_protocol = "HTTP"
    }
  }

  ingress_rules = [
    {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]

  egress_rules = [
    {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]
}

#Microservices
microservice_config = {
  "candidatos-qry" = {
    name             = "candidatos-qry"
    is_public        = true
    container_port   = 80
    host_port        = 80
    cpu              = 256
    memory           = 512
    desired_count    = 1
    alb_target_group = {
      port              = 80
      protocol          = "HTTP"
      path_pattern      = ["/candidates*"]
      health_check_path = "/candidates/ping"
      priority          = 1
    }
    auto_scaling = {
      max_capacity = 2
      min_capacity = 1
      cpu          = {
        target_value = 75
      }
      memory = {
        target_value = 75
      }
    }
  },
  "pruebas-qry" = {
    name             = "pruebas-qry"
    is_public        = false
    container_port   = 80
    host_port        = 80
    cpu              = 256
    memory           = 512
    desired_count    = 1
    alb_target_group = {
      port              = 80
      protocol          = "HTTP"
      path_pattern      = ["/pruebas-query*"]
      health_check_path = "/pruebas-query/ping"
      priority          = 1
    }
    auto_scaling = {
      max_capacity = 2
      min_capacity = 1
      cpu          = {
        target_value = 75
      }
      memory = {
        target_value = 75
      }
    }
  },
  "preguntas-qry" = {
    name             = "preguntas-qry"
    is_public        = false
    container_port   = 80
    host_port        = 80
    cpu              = 256
    memory           = 512
    desired_count    = 1
    alb_target_group = {
      port              = 80
      protocol          = "HTTP"
      path_pattern      = ["/preguntas-query*"]
      health_check_path = "/preguntas-query/ping"
      priority          = 1
    }
    auto_scaling = {
      max_capacity = 2
      min_capacity = 1
      cpu          = {
        target_value = 75
      }
      memory = {
        target_value = 75
      }
    }
  }
}