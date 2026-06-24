# TECH_SPEC.md

## Technical Specification for Data Sifter

### Architecture Overview

Data Sifter is designed as a modular and scalable application that enables users to visually construct workflows for data scraping tasks. The architecture is divided into three main layers:

1. **User Interface Layer**: This layer provides a graphical interface where users can interactively design their data scraping workflows using drag-and-drop functionality. It communicates with the Workflow Engine through a set of well-defined APIs.

2. **Workflow Engine Layer**: This layer processes the user-defined workflows. It interprets the JSON representation of the workflow, executes the corresponding data scraping tasks, and manages the flow of data between different blocks.

3. **Data Processing Layer**: This layer handles the actual data scraping and processing tasks. It includes various scrapers and processors that can be invoked by the Workflow Engine based on the workflow definition.

### Components

#### User Interface Component

- **Canvas**: A visual workspace where users can add, move, and connect blocks representing different data scraping actions.
- **Block Library**: A collection of predefined blocks that users can drag onto the canvas. Each block represents a specific action or operation in the data scraping process.
- **JSON Serializer/Deserializer**: Converts the visual workflow into a JSON format for storage and execution, and vice versa.

#### Workflow Engine Component

- **Workflow Interpreter**: Parses the JSON workflow definition and translates it into executable instructions.
- **Task Scheduler**: Manages the execution order of tasks within the workflow, ensuring that dependencies are respected.
- **Data Flow Manager**: Coordinates the transfer of data between different blocks in the workflow.

#### Data Processing Component

- **Scrapers**: Implementations of various web scraping techniques tailored to different types of data sources.
- **Processors**: Tools for cleaning, transforming, and analyzing the scraped data according to the workflow specifications.

### Data Model

The core data model of Data Sifter revolves around the concept of a "workflow". A workflow is represented as a directed graph where nodes are blocks and edges represent data flow between blocks. Each block has a type and a set of configurable parameters.

```json
{
  "blocks": [
    {
      "id": "block1",
      "type": "web_scraper",
      "params": {
        "url": "http://example.com",
        "selector": ".content"
      }
    },
    {
      "id": "block2",
      "type": "data_processor",
      "params": {
        "operation": "filter",
        "criteria": "price > 100"
      }
    }
  ],
  "connections": [
    {
      "from": "block1",
      "to": "block2"
    }
  ]
}
```

### Key APIs/Interfaces

#### User Interface APIs

- `createBlock(type, params)`: Adds a new block of the specified type with given parameters to the canvas.
- `connectBlocks(fromId, toId)`: Creates a connection between two blocks, defining the data flow direction.
- `serializeWorkflow()`: Converts the current state of the canvas into a JSON workflow definition.
- `deserializeWorkflow(json)`: Loads a workflow from a JSON string and updates the canvas accordingly.

#### Workflow Engine APIs

- `executeWorkflow(json)`: Takes a JSON workflow definition and executes it, returning the final processed data.
- `getExecutionStatus(workflowId)`: Retrieves the status of a running workflow.

### Tech Stack

- **Frontend**: React.js for building the interactive user interface.
- **Backend**: Node.js with Express.js for handling server-side logic and API endpoints.
- **Data Scraping**: Puppeteer for web scraping tasks.
- **Data Processing**: Pandas for data manipulation and analysis.

### Dependencies

- **React.js**: For building the user interface.
- **Node.js & Express.js**: For backend services.
- **Puppeteer**: For web scraping capabilities.
- **Pandas**: For data processing tasks.
- **pgvector**: For storing and querying the company's knowledge base and datasets.

### Deployment

Data Sifter is deployed as a web application. The frontend is built using React.js and served statically. The backend, built with Node.js and Express.js, is hosted on a cloud platform such as AWS or Google Cloud Platform. The application uses a PostgreSQL database with pgvector extension for efficient data storage and retrieval.

To deploy Data Sifter:

1. Build the frontend using `npm run build`.
2. Deploy the built frontend files to a static hosting service.
3. Deploy the backend server to a cloud platform, configuring environment variables for database connections and other settings.
4. Set up a PostgreSQL database with pgvector extension and import necessary datasets.
5. Configure the backend to connect to the database and start the server.

This deployment setup ensures high availability and scalability, allowing Data Sifter to handle a large number of concurrent users and complex data scraping workflows efficiently.
