
import multiprocessing


def skill_data():
    return [
        {
            "skill": "3",
            "description": "",
            "exam_total_items": 50,
            "reviewer_total_items": 150,
            "duration_minutes": 0,
            "duration_hours": 1,
        },
        {
            "skill": "5",
            "description": "",
            "exam_total_items": 75,
            "reviewer_total_items": 175,
            "duration_minutes": 30,
            "duration_hours": 1,
        },
        {
            "skill": "7",
            "description": "",
            "exam_total_items": 100,
            "reviewer_total_items": 200,
            "duration_minutes": 0,
            "duration_hours": 2,

        },
        {
            "skill": "9",
            "description": "",
            "exam_total_items": 100,
            "reviewer_total_items": 200,
            "duration_minutes": 0,
            "duration_hours": 2,

        },
        {
            "skill": "AFSC 10070/10090",
            "description": "First Sgt/Sgt Major AFSC",
            "exam_total_items": 50,
            "reviewer_total_items": 150,
            "duration_minutes": 0,
            "duration_hours": 1,

        },
    ]

def process_skill_data(data):
    print(data)

def process():
    try:
        # Use multiprocessing Pool to parallelize the processing of skill data
        with multiprocessing.Pool() as pool:
            pool.map(process_skill_data, skill_data())

        print("Data import successful.")
    except Exception as e:
        print(f"Error during data import: {str(e)}")

# SAMPLE USAGE
if __name__ == "__main__":
    process()
    # SABAY SABAY I PROCESS LAHAT TAPOS I PRINT PAG TAPOS NA LAHAT NG PROCESSING

    # OUTPUT 
    """
    D:\PycharmProjects\skaty\venv\Scripts\python.exe D:\PycharmProjects\skaty\exam\scripts\sample_multiprocessing.py 
    {'skill': '3', 'description': '', 'exam_total_items': 50, 'reviewer_total_items': 150, 'duration_minutes': 0, 'duration_hours': 1}
    {'skill': '5', 'description': '', 'exam_total_items': 75, 'reviewer_total_items': 175, 'duration_minutes': 30, 'duration_hours': 1}
    {'skill': '7', 'description': '', 'exam_total_items': 100, 'reviewer_total_items': 200, 'duration_minutes': 0, 'duration_hours': 2}
    {'skill': '9', 'description': '', 'exam_total_items': 100, 'reviewer_total_items': 200, 'duration_minutes': 0, 'duration_hours': 2}
    {'skill': 'AFSC 10070/10090', 'description': 'First Sgt/Sgt Major AFSC', 'exam_total_items': 50, 'reviewer_total_items': 150, 'duration_minutes': 0, 'duration_hours': 1}
    Data import successful.
    
    Process finished with exit code 0
    """
    # End of Terminal Input
    
