import unittest

from src.classes.docker_engine import DockerEngine


class DockerEngineTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(DockerEngineTests, self).__init__(*args, **kwargs)

    def test_get_client(self):
        client = DockerEngine().get_client()
        self.assertNotEqual(client, None, 'Engine does not exist')

    def test_run_hello_world_image(self):
        response = DockerEngine().run_container_operation(
            operation='run',
            data={
                'image': 'hello-world'
            }
        )
        self.assertNotEqual(response.decode().find('Hello from Docker!'), -1,
                            'Hello world run failed')

    def test_run_and_stop_background_container(self):
        response = DockerEngine().run_container_operation(
            operation='run',
            data={
                'image': 'mongo:4.2.3',
                'detach': True
            }
        )
        self.assertNotEqual(response, None, 'Background image run failed')
        self.assertEqual(response.status, 'created', 'Image not created')

        container = DockerEngine().get_container_by_id(response.short_id)
        self.assertNotEqual(container, None, 'Container does not exist')

        response = DockerEngine().run_operation_in_object(
            thing=container,
            operation='stop',
            data={}
        )

        self.assertEqual(response, None, 'Image not stopped')

    def test_pull_image(self):
        response = DockerEngine().run_image_operation(
            operation='pull',
            data={
                'repository': 'alpine:latest'
            }
        )
        self.assertNotEqual(response, None, 'Pull image failed')

    def test_remove_image(self):
        response = DockerEngine().run_image_operation(
            operation='remove',
            data={
                'image': 'alpine',
                'force': True
            }
        )
        self.assertEqual(response, None, 'Remove image failed')
