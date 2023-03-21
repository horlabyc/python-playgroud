import datetime

class StockItem:
    def __init__(self, item_name, item_category, quantity, 
                 created_at=None, updated_at=None, id=None
                ):
        self.item_name = item_name
        self.item_category = item_category
        self.created_at = created_at if created_at is not None else datetime.datetime.now().isoformat()
        self.updated_at = updated_at if updated_at is not None else datetime.datetime.now().isoformat()
        self.quantity = quantity
        self.id = id if id is not None else None
    
    def __repr__(self) -> str:
        return f"({self.item_name}, {self.item_category}, {self.quantity}, {self.created_at}, {self.updated_at}, {self.id})"