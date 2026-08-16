---
### 👤 Author Information

* **Developer:** Sabih Maqsood
* **Email:** ansarisabih32@gmail.com
* **Social Handles:** LinkedIn / GitHub / Kaggle / Facebook / Instagram (`@sabihmaqsood`)

---
#  Topic: Core Foundations & Data Schemas (The Prerequisites)

## 📖 Overview & Description

LLMs by default plain text generate kartay hain, jo human readability ke liye acha hota ha magar programmatic pipelines ke liye unpredictable ha. **Structured Output** ka maqsad LLM se predictable, type-safe data (jaise JSON ya Pydantic objects) hasil karna ha takay application code bina text parsing ke directly response read kar sakay.

LangChain me structured output define karne ke liye **3 Primary Schema Styles** use hote hain:

1. **Pydantic Models (v2):** Production-ready schema design, dynamic runtime data validation, constraints, aur default values ke saath.
2. **TypedDict:** Lightweight Python dictionary structure, prototyping ke liye best.
3. **JSON Schema:** Plain dictionary-based universal format, jo programming language independent hota ha.

---

## 📊 Schema Styles Comparison Table

| Feature | Pydantic (v2)

 | TypedDict

 | JSON Schema

|                                   |                        |  |  |
| --------------------------------- | ---------------------- | - | - |
| **Runtime Data Validation** | ✅ Yes (strict checks) |  |  |

 | ❌ No (typing hints only)

 | ❌ No (requires parser)

 |
| **Type Coercion (e.g. "32" -> 32)** | ✅ Automatic

 | ❌ Manual

 | ❌ Manual

 |
| **Field Descriptions & Constraints** | ✅ Supported (`Field()`)

 | ⚠️ Limited (`Annotated`)

 | ✅ Supported (`description`)

 |
| **Return Type** | Pydantic Instance

 | Python `dict` | Python `dict` |
| **Best Used For** | Production applications

 | Quick scripts & prototypes

 | Cross-language / dynamic schemas

 |

---

### 1️⃣ `pydantic_demo.py` (Pydantic v2 Schema)

```python
"""
Pydantic v2 Data Schema Definition
Includes constraints, descriptions, type validation, and JSON serialization.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class Student(BaseModel):
    name: str = Field(default="Nitish", description="Full name of the student")
    age: Optional[int] = Field(default=None, description="Age in years")
    email: EmailStr = Field(description="Valid email address")
    cgpa: float = Field(
        default=5.0, 
        gt=0, 
        lt=10, 
        description="A decimal value representing student CGPA (0 to 10)"
    )

# Validating input data dynamically
student_data = {"age": "32", "email": "student@gmail.com"}
student = Student(**student_data)

# Accessing attributes and converting to JSON
print(f"Validated Student Age: {student.age}")
print("Pydantic JSON Serialized Output:")
print(student.model_dump_json(indent=2))
```

---

### 2️⃣ `typeddict_demo.py` (TypedDict Schema)

```python
"""
TypedDict Schema Definition
Lightweight dictionary layout with Annotated field descriptions.
"""

from typing import TypedDict, Annotated, Optional

class StudentTypedDict(TypedDict):
    name: Annotated[str, "Full name of the student"]
    age: Annotated[Optional[int], "Age of the student"]
    email: Annotated[str, "Contact email address"]
    cgpa: Annotated[float, "Student CGPA score"]

# Creating a compliant dictionary instance
student_dict: StudentTypedDict = {
    "name": "Nitish",
    "age": 35,
    "email": "nitish@example.com",
    "cgpa": 8.5
}

print("TypedDict Output Dictionary:")
print(student_dict)
```

---

### 3️⃣ `json_schema_demo.py` (JSON Schema)

```python
"""
JSON Schema Definition
Universal dictionary schema format independent of Python classes.
"""

import json

student_json_schema = {
    "title": "student",
    "description": "Schema definition for student records",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Full name of the student"
        },
        "age": {
            "type": "integer",
            "description": "Age of the student in years"
        },
        "email": {
            "type": "string",
            "description": "Valid contact email"
        },
        "cgpa": {
            "type": "number",
            "description": "CGPA score between 0 and 10"
        }
    },
    "required": ["name", "email"]
}

print("JSON Schema Definition:")
print(json.dumps(student_json_schema, indent=2))
```

---

### 🎯 Key Takeaway

* **Pydantic** is the primary choice for building real-world LLM applications because it ensures data integrity before it enters your backend logic.
* **TypedDict** and **JSON Schema** offer lightweight and portable alternatives when strict validation isn't mandatory or schemas are built dynamically.
