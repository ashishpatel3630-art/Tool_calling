def get_student(student_id: int) -> dict:
    """
    Get student information using student ID.
    """

    students = {

        101: {
            "name": "Rahul",
            "course": "B.Tech",
            "marks": 82
        },

        102: {
            "name": "Amit",
            "course": "BCA",
            "marks": 76
        },

        103: {
            "name": "Priya",
            "course": "B.Tech",
            "marks": 91
        }
    }

    return students.get(
        student_id,
        {
            "error": "Student not found"
        }
    )