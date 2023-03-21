import datetime

class Todo:
  def __init__(self, task, category, 
               created_at=None, completed_at=None, 
               status=None, id=None
              ):
    self.task = task
    self.category = category
    self.created_at = created_at if created_at is not None else datetime.datetime.now().isoformat()
    self.completed_at = completed_at if completed_at is not None else None
    self.status = status if status is not None else 1 # 1 = open, 2 = completed
    self.id = id if id is not None else None
  
  def __repr__(self) -> str:
    return f"({self.task}, {self.category}, {self.created_at}, {self.completed_at}, {self.status}, {self.id})"