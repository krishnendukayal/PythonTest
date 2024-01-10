def find_runner_up_score(scores):
    unique_scores = list(set(scores))  # Remove duplicate scores
    unique_scores.sort(reverse=True)   # Sort scores in descending order

    # Check if there is a runner-up
    if len(unique_scores) > 1:
        runner_up_score = unique_scores[1]
        return runner_up_score
    else:
        return "No runner-up score available."

# Example usage:
if __name__ == "__main__":
    try:
        scores = list(map(int, input("Enter the scores separated by space: ").split()))
        runner_up_score = find_runner_up_score(scores)
        print(f"The runner-up score is: {runner_up_score}")
    except ValueError:
        print("Invalid input. Please enter numerical scores separated by space.")