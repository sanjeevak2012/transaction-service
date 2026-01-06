from fastapi import FastAPI

app = FastAPI(title="Transaction Service")

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/transaction/{txn_id}")
def transaction_status(txn_id: str):
    return {
        "transaction_id": txn_id,
        "status": "SUCCESS",
        "amount": 2500,
        "currency": "INR"
    }
