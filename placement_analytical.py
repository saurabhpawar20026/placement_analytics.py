import pandas as pd

# Creating a sample dataset for the project
def create_sample_data():
    data = {
        'Student_Name': ['Rahul', 'Sneha', 'Amit', 'Priya', 'Vikram'],
        'Department': ['MCA', 'BCA', 'MCA', 'BTech', 'MCA'],
        'CGPA': [8.5, 7.2, 9.0, 6.8, 8.1],
        'Technical_Score': [85, 60, 92, 55, 78],
        'Status': ['Placed', 'Not Placed', 'Placed', 'Not Placed', 'Placed']
    }
    df = pd.DataFrame(data)
    df.to_csv('placement_data.csv', index=False)
    print("Dataset created: placement_data.csv\n")

# Analyzing placement data
def analyze_placement():
    df = pd.read_csv('placement_data.csv')
    
    print("--- Placement Drive Statistics ---")
    print(f"Total Students: {len(df)}")
    
    placed_count = df[df['Status'] == 'Placed'].shape[0]
    print(f"Students Placed: {placed_count}")
    
    avg_cgpa = df['CGPA'].mean()
    print(f"Average CGPA of Batch: {avg_cgpa:.2f}")
    
    # Filtering top performers
    top_performers = df[df['Technical_Score'] > 80]
    print("\nTop Performers (Technical Score > 80):")
    print(top_performers[['Student_Name', 'Technical_Score']])

if __name__ == "__main__":
    create_sample_data()
    analyze_placement()
