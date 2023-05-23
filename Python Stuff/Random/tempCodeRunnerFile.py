import bedrock
from setuptools import setup

setup(name="bedrock",
      version="0.1",
      description="A simply python library to access Minecraft: Bedrock Edition worlds.",
      keywords="minecraft bedrock leveldb",
      url="https://github.com/BluCodeGH/bedrock",
      packages=["bedrock"],
      install_requires=["numpy"],
      package_data={
          "bedrock": ["*.dll", "*.so", "LICENCE-LEVELDB"]
      },
      author="BluCode")

with bedrock.World("My World.mcworld") as world:
    block = bedrock.Block("minecraft:stone") # Name must include `minecraft:`
    world.setBlock(0, 0, 0, block)
    block = bedrock.Block("minecraft:stone", 2) # Data value
    world.setBlock(0, 1, 0, block)
    if world.getBlock(0, 2, 0).name == "minecraft:stone":
        print("More stone!")
