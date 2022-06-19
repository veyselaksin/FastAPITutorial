from typing import Optional, Union
from fastapi import FastAPI
 
app = FastAPI()


@app.get("/api/v1/blogs")
def blogs(limit=10, published: bool = True, sort: Optional[str] = None):

    if published:
        return {
            "status": 200,
            "details": "OK",
            "data": [
                {
                    "id": "1", 
                    "title":"Title", 
                    "body": "Body", 
                    "comments": [
                        {"id": "1", "comment":"Just comment"},
                        {"id": "2", "comment":"Just comment"},
                        {"id": "3", "comment":"Just comment"},
                        {"id": "4", "comment":"Just comment"},
                        {"id": "5", "comment":"Just comment"},
                        {"id": "6", "comment":"Just comment"},
                        {"id": "7", "comment":"Just comment"}
                    ]
                },
                {
                    "id": "2", 
                    "title":"Title", 
                    "body": "Body", 
                    "comments": [
                        {"id": "1", "comment":"Just comment"},
                        {"id": "2", "comment":"Just comment"},
                        {"id": "3", "comment":"Just comment"},
                        {"id": "4", "comment":"Just comment"},
                        {"id": "5", "comment":"Just comment"},
                        {"id": "6", "comment":"Just comment"},
                        {"id": "7", "comment":"Just comment"}
                    ]
                },
                {
                    "id": "3", 
                    "title":"Title", 
                    "body": "Body", 
                    "comments": [
                        {"id": "1", "comment":"Just comment"},
                        {"id": "2", "comment":"Just comment"},
                        {"id": "3", "comment":"Just comment"},
                        {"id": "4", "comment":"Just comment"},
                        {"id": "5", "comment":"Just comment"},
                        {"id": "6", "comment":"Just comment"},
                        {"id": "7", "comment":"Just comment"}
                    ]
                },
                {
                    "id": "4", 
                    "title":"Title", 
                    "body": "Body", 
                    "comments": [
                        {"id": "1", "comment":"Just comment"},
                        {"id": "2", "comment":"Just comment"},
                        {"id": "3", "comment":"Just comment"},
                        {"id": "4", "comment":"Just comment"},
                        {"id": "5", "comment":"Just comment"},
                        {"id": "6", "comment":"Just comment"},
                        {"id": "7", "comment":"Just comment"}
                    ]
                }

            ]
        }
    else:
        return {
            "status": 200,
            "details": "OK",
            "data": [
                {
                    "id": "1", 
                    "title":"Title", 
                    "body": "Body", 
                    "comments": [
                        {"id": "1", "comment":"Just comment"},
                        {"id": "2", "comment":"Just comment"},
                        {"id": "3", "comment":"Just comment"},
                        {"id": "4", "comment":"Just comment"},
                        {"id": "5", "comment":"Just comment"},
                        {"id": "6", "comment":"Just comment"},
                        {"id": "7", "comment":"Just comment"}
                    ]
                },
                {
                    "id": "2", 
                    "title":"Title", 
                    "body": "Body", 
                    "comments": [
                        {"id": "1", "comment":"Just comment"},
                        {"id": "2", "comment":"Just comment"},
                        {"id": "3", "comment":"Just comment"},
                        {"id": "4", "comment":"Just comment"},
                        {"id": "5", "comment":"Just comment"},
                        {"id": "6", "comment":"Just comment"},
                        {"id": "7", "comment":"Just comment"}
                    ]
                },
            ]
        }


@app.get("/api/v1/blog/unpublished")
def unpublished():
    return {
        "status": 200,
        "details": "OK",
        "data": "all unpublished blogs"
    }


@app.post("/api/v1/blog")
def create_blog():
    return {
        "status": 201,
        "details": "Created",
        "message": "Blog is created"
    }


@app.get("/api/v1/blog/{id}")
def blog(id: int):
    return {
        "status": 200,
        "details": "OK",
        "data": f"blog {id}"
    }


@app.get("/api/v1/blog/{id}/comments")
def blog_comments(id: int):
    return {
        "status": 200,
        "details": "OK",
        "data": f"comments for blog {id}"
    }