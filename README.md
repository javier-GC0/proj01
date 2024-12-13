## Project structure

- **config**: 
    - **config.yaml**: Contains all the configuration parameters for the application, logging settings, intervals, and others.
  
- **data**: Stores application data output in a text file (`data.txt`). The default file path is specified in `config.yaml`.

- **logs**: Stores log file (`project.log`) generated during the application's execution. The log format, level, and location are configured in `config.yaml`.

- **src**:
    - **client.py**: Implements the `DataClient` class, which is responsible for fetching data from an external source and processing it.
    - **file_handler.py**: Defines the `FileHandler` class, used for managing file-based operations, such as reading and writing data.
    - **get_data.py**: Contains the `ApiData` class, which interacts with an external API to fetch data in real-time.
    - **logging_handler.py**: Provides the `LoggerConfig` class, used to configure and manage the logging system for the application.
    - **main.py**: The entry point of the application, managing the initialization of components and starting the processes.
- **setup.py**: Handles the configuration of the project. It loads the `config.yaml` file and sets up the parameters.