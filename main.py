from fastapi import FastAPI

app = FastAPI()

cursos = {
  1: {
    "titulo": "Teste 1",
    "aulas": 5,
    "horas": 10
  },
  2: {
    "titulo": "Teste 2",
    "aulas": 10,
    "horas": 20
  }
}

@app.get('/')
async def raiz():
  return {"msg": "Hello World_"}

@app.get('/cursos')
async def getCursos():
  return cursos

@app.get('/cursos/{curso_id}')
async def getCurso(curso_id: int):
  curso = cursos[curso_id]
  return curso

if __name__ == '__main__':
  import uvicorn
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)