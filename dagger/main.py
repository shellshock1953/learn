import random

import dagger
from dagger import dag, function, object_type




@object_type
class HelloDagger:
    @function
    async def publish(self, source: dagger.Directory) -> str:
        """Publish the application container after building and testing it on-the-fly"""
        await self.test(source)
        return await self.build(source).publish(
            f"ttl.sh/myapp-{random.randrange(10 ** 8)}"
        )

    @function
    def build_env(self, source: dagger.Directory) -> dagger.Container:
        """Build a ready-to-use development environment"""
        # create a Dagger cache volume for dependencies
        node_cache = dag.cache_volume("node")
        return (
            dag.container()
            # start from a base Node.js container
            .from_("node:21-slim")
            # add the source code at /src
            .with_directory("/src", source)
            # mount the cache volume at /src/node_modules
            .with_mounted_cache("/src/node_modules", node_cache)
            # change the working directory to /src
            .with_workdir("/src")
            # run npm install to install dependencies
            .with_exec(["npm", "install"])
        )

    @function
    async def test(self, source: dagger.Directory) -> str:
        """Return the result of running unit tests"""
        return (
            await (
                # get the build environment container
                # by calling another Dagger Function
                self.build_env(source)
                # call the test runner
                .with_exec(["npm", "run", "test:unit", "run"])
                # capture and return the command output
                .stdout()
            )
        )

    @function
    def build(self, source: dagger.Directory) -> dagger.Container:
        """Build the application container"""
        build = (
            # get the build environment container
            # by calling another Dagger Function
            self.build_env(source)
            # build the application
            .with_exec(["npm", "run", "build"])
            #  get the build output directory
            .directory("./dist")
        )
        return (
            dag.container()
            # start from a slim NGINX container
            .from_("nginx:1.25-alpine")
            # copy the build output directory to the container
            .with_directory("/usr/share/nginx/html", build)
            # expose the container port
            .with_exposed_port(80)
        )
