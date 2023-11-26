## Todo List with DB

todo list program with SQLite
- [`sqlite3` module](https://docs.python.org/ko/3.8/library/sqlite3.html#)



CRUD 중 `Create`는 할일 추가 기능, `Read`는 할일 목록 조회 기능, `Update`는 할일 완료 여부 수정 기능, `Delete`는 할일 삭제 기능과 대응된다.

| CRUD   | Function           | SQL Query |
|--------|--------------------|-----------|
| Create | Add Todo           | INSERT    |
| Read   | Get Todos          | SELECT    |
| Update | Update Done Status | UPDATE    |
| Delete | Delete Todo        | DELETE    |