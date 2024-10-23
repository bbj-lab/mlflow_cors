from setuptools import setup

setup(
    name="mlflow_cors",
    install_requires=[
        'flask-cors',
    ],
    entry_points="""
        [mlflow.app]
        mlflow_cors=mlflow_cors:create_app
    """
)