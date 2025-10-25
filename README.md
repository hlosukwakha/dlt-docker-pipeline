
# 🚀 DLT Docker Pipeline — Hacker News → Postgres

![DLT Pipeline](https://img.shields.io/badge/DLT-Pipeline-blue?logo=docker&style=for-the-badge)

---

## 📝 About this Project

This project demonstrates how to build a **data pipeline** using [DLT (Data Load Tool)](https://dlthub.com) and run it seamlessly inside **Docker**.  
It fetches the **top Hacker News stories** using the official HN API and loads them into a **PostgreSQL** database running as a container.

It’s a simple, modular, and reproducible ELT pipeline showcasing how modern data stacks can be minimal yet powerful.  
Perfect for students, data engineers, and hobbyists looking to understand **data ingestion and transformation** in a containerized setup.

> “DLT is to data what Flask is to web apps — lightweight, elegant, and developer‑friendly.”

---

## 🧠 Technology Stack

| Layer | Tool / Framework | Purpose |
|-------|------------------|----------|
| **Ingestion** | `requests`, `DLT` | Fetch data and orchestrate pipeline |
| **Transformation** | `DLT` schema & normalization | Handle JSON schema evolution automatically |
| **Storage** | `PostgreSQL` | Store structured data |
| **Orchestration** | `Docker`, `docker-compose` | Container management |
| **Language** | `Python 3.11` | Core implementation |

---

## 📊 Dataset: Hacker News Top Stories

The dataset comes from the **Hacker News REST API**:

- Endpoint: `https://hacker-news.firebaseio.com/v0/topstories.json`
- Each story ID is expanded via: `https://hacker-news.firebaseio.com/v0/item/{id}.json`
- Data includes:
  - `id`, `title`, `by`, `score`, `url`, `time`, `descendants`
  - `type` (e.g., story, job, comment)

DLT automatically infers the schema and loads it into PostgreSQL under `hn_raw.stories`.

---

## 🪣 Project Structure

```
dlt-docker-pipeline/
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ dlt.yml
├─ .env.example
├─ .gitignore
├─ Makefile
└─ src/
   ├─ __init__.py
   └─ pipeline.py
```

---

## 🧰 Getting Started

### 1️⃣ Clone the Project

```bash
git clone https://github.com/hlosukwakha/dlt-docker-pipeline.git
cd dlt-docker-pipeline
```

### 2️⃣ Set Up Environment

```bash
cp .env.example .env
```

Default configuration (already works for Docker Compose setup):

```env
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=dlt
POSTGRES_USER=dlt
POSTGRES_PASSWORD=dlt
```

### 3️⃣ Build and Run Containers

```bash
docker compose up -d --build
```

### 4️⃣ Watch Logs

```bash
docker compose logs -f dlt-runner
```

### 5️⃣ Inspect Data in Postgres

```bash
docker compose exec -T postgres psql -U dlt -d dlt -c "\dt hn_raw.*"
```

---

## ⚙️ Useful Commands

| Command | Description |
|----------|--------------|
| `make up` | Build and start containers |
| `make down` | Stop and remove containers |
| `make run` | Run pipeline once |
| `make logs` | Tail logs |
| `make bash` | Enter the DLT runner shell |
| `make reset` | Clean everything |

---

## ✍️ Blog‑Style Note

> “The beauty of DLT is its simplicity — it lets data engineers focus on logic, not plumbing.  
> Combine it with Docker and you get a reproducible, portable data environment that runs anywhere.  
> This project takes one of the most public APIs (Hacker News) and shows how fast you can turn raw JSON into queryable analytics tables.”

---

## 🗓️ Last Updated
**October 25, 2025**

---

**Author:** Mpumelelo Ndlovu (@hlosukwakha)  
**License:** MIT  
**Powered by:** [DLT](https://dlthub.com), [Docker](https://www.docker.com), [PostgreSQL](https://www.postgresql.org)
