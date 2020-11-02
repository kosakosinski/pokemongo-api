from setuptools import setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

requirements_path = "./requirements.txt"

install_reqs = parse_requirements(requirements_path, session=False)

try:
    reqs = [str(ir.requirement) for ir in install_reqs]
except:
    reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='pogo',
    version='0.0.1',
    packages=[
        'pogo', 'POGOProtos', 'POGOProtos.Map', 'POGOProtos.Map.Fort',
        'POGOProtos.Map.Pokemon', 'POGOProtos.Data', 'POGOProtos.Data.Gym',
        'POGOProtos.Data.Logs', 'POGOProtos.Data.Battle',
        'POGOProtos.Data.Player', 'POGOProtos.Data.Capture',
        'POGOProtos.Enums', 'POGOProtos.Settings',
        'POGOProtos.Settings.Master', 'POGOProtos.Settings.Master.Item',
        'POGOProtos.Settings.Master.Pokemon', 'POGOProtos.Inventory',
        'POGOProtos.Inventory.Item', 'POGOProtos.Networking',
        'POGOProtos.Networking.Requests',
        'POGOProtos.Networking.Requests.Messages',
        'POGOProtos.Networking.Envelopes', 'POGOProtos.Networking.Responses'
    ],
    url='https://github.com/rubenvereecken/pokemongo-api',
    license='',
    author='',
    author_email='',
    description='PokemonGO API for Python',
    install_requires=reqs
)
