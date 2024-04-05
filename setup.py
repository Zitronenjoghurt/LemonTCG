from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="lemon_tcg",
    python_requires=">=3.9",
    version="0.1.1",
    packages=find_packages(),
    license="GNU General Public License v3.0",
    description="A library providing the game logic for the LemonTCG online multiplayer TCG game.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Zitronenjoghurt",
    install_requires=[
        'pydantic==2.6.4'
    ],
    extras_require={'dev': ['pytest', 'coverage', 'pytest-cov', 'twine', 'wheel']},
    url="https://github.com/Zitronenjoghurt/LemonTCG"
)