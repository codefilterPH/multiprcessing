
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

def process_skill_data(self, data):
    print(data)

def process(self):
    try:
        # Use multiprocessing Pool to parallelize the processing of skill data
        with multiprocessing.Pool() as pool:
            pool.map(self.process_skill_data, self.skill_data())

        print("Data import successful.")
    except Exception as e:
        print(f"Error during data import: {str(e)}")


