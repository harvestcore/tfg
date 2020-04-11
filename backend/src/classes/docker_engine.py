import docker

from config.server_environment import DOCKER_BASE_URL


class DockerEngine:
    client = docker.DockerClient(base_url=DOCKER_BASE_URL)
    engine = None

    def __new__(cls, *args, **kwargs):
        if not cls.engine:
            cls.engine = super(DockerEngine, cls).__new__(cls, *args, **kwargs)
        return cls.engine

    def get_client(self):
        return self.client if self.engine else None

    def run_container_operation(self, operation, data):
        try:
            return getattr(self.get_client().containers, operation)(**data)
        except docker.errors.APIError:
            return False

    def run_image_operation(self, operation, data):
        try:
            return getattr(self.get_client().images, operation)(**data)
        except docker.errors.APIError:
            return False

    def get_container_by_id(self, container_id):
        try:
            return self.get_client().containers.get(container_id=container_id)
        except docker.errors.APIError:
            return False

    @staticmethod
    def run_operation_in_object(object, operation, data):
        try:
            return getattr(object, operation)(**data)
        except docker.errors.APIError:
            return False

    def get_image_by_name(self, name):
        try:
            return self.get_client().images.get(name=name)
        except docker.errors.APIError:
            return False
