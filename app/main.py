from fastapi import FastAPI
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from app.agents.research_agent import create_research_agent
import uuid

app = FastAPI(title="PatentSense", version="0.1.0")

agent = create_research_agent()
session_service = InMemorySessionService()
runner = Runner(agent=agent, session_service=session_service, app_name="patent_sense")


class QueryRequest(BaseModel):
    query: str
    user_id: str = "default_user"
    session_id: str | None = None


@app.post("/research")
async def research(request: QueryRequest):
    session_id = request.session_id or str(uuid.uuid4())

    # Create session if it doesn't exist
    session = await session_service.create_session(
        app_name="patent_sense", user_id=request.user_id, session_id=session_id
    )

    # IMPORTANT: new_message must be a Content object, not a string
    new_message = types.Content(role="user", parts=[types.Part(text=request.query)])

    final_response = ""
    async for event in runner.run_async(
        user_id=request.user_id, session_id=session.id, new_message=new_message
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    final_response = part.text

    return {"session_id": session.id, "response": final_response}


@app.get("/")
def root():
    return {"message": "PatentSense is running"}
