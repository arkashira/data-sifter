```markdown
# Dataflow Architecture for Data-Sifter

## External Data Sources
- Websites (HTML pages, APIs)
- Public datasets
- User-uploaded files (CSV, JSON)

## Ingestion Layer
- **Components:**
  - Web Scraper Module
    - Responsible for fetching data from specified URLs.
    - Handles rate limiting and retries.
  - API Connector
    - Interfaces with RESTful APIs to pull data.
  - File Uploader
    - Allows users to upload files for processing.
- **Auth Boundary:**
  - User authentication (OAuth2, API keys) to access external APIs and upload files.

## Processing/Transform Layer
- **Components:**
  - Data Parser
    - Extracts relevant information from HTML, JSON, or CSV formats.
  - Data Cleaner
    - Removes duplicates, normalizes data formats, and handles missing values.
  - Data Enricher
    - Augments data with additional context or metadata (e.g., geolocation, timestamps).
- **Auth Boundary:**
  - Internal service authentication to ensure secure data processing.

## Storage Tier
- **Components:**
  - Raw Data Store (e.g., S3, Blob Storage)
    - Stores unprocessed data for future reference.
  - Processed Data Store (e.g., SQL/NoSQL database)
    - Stores cleaned and enriched data for querying.
- **Auth Boundary:**
  - Role-based access control (RBAC) to manage permissions for data access.

## Query/Serving Layer
- **Components:**
  - Query Engine
    - Allows users to run SQL-like queries against the processed data.
  - API Gateway
    - Serves as the interface for users to access the data via RESTful APIs.
- **Auth Boundary:**
  - User authentication and authorization checks for API access.

## Egress to User
- **Components:**
  - Data Exporter
    - Facilitates exporting data in various formats (CSV, JSON, Excel).
  - Dashboard/Visualization Tool
    - Provides a user interface for data analysis and visualization.
- **Auth Boundary:**
  - User session management to ensure secure access to the dashboard and export functionalities.

```

### ASCII Block Diagram
```
+---------------------+
|  External Data      |
|  Sources            |
|  (Websites, APIs,   |
|  User Files)        |
+----------+----------+
           |
           v
+---------------------+
|  Ingestion Layer    |
|  (Web Scraper,      |
|  API Connector,     |
|  File Uploader)     |
+----------+----------+
           |
           v
+---------------------+
|  Processing/Transform|
|  Layer              |
|  (Data Parser,      |
|  Data Cleaner,      |
|  Data Enricher)     |
+----------+----------+
           |
           v
+---------------------+
|  Storage Tier       |
|  (Raw Data Store,   |
|  Processed Data Store)|
+----------+----------+
           |
           v
+---------------------+
|  Query/Serving Layer|
|  (Query Engine,     |
|  API Gateway)       |
+----------+----------+
           |
           v
+---------------------+
|  Egress to User     |
|  (Data Exporter,    |
|  Dashboard)         |
+---------------------+
```