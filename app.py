import streamlit as st


def grade_from_percent(p: float) -> str:
	if p >= 90:
		return "A+"
	if p >= 80:
		return "A"
	if p >= 70:
		return "B"
	if p >= 60:
		return "C"
	if p >= 50:
		return "D"
	return "F"


def main() -> None:
	st.set_page_config(page_title="Marks Percentage & Grade Calculator", layout="centered")
	st.title("Marks Percentage & Grade Calculator")

	subjects = st.number_input("Number of subjects", min_value=1, max_value=50, value=3, step=1)

	st.markdown("---")

	marks = []
	cols = st.columns(2)
	for i in range(1, int(subjects) + 1):
		key = f"mark_{i}"
		# place inputs alternately in two columns for compact layout
		col = cols[(i - 1) % 2]
		m = col.number_input(f"Subject {i} marks (0-100)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, key=key)
		marks.append(m)

	st.markdown("---")

	if st.button("Calculate"):
		total = sum(marks)
		num = len(marks)
		if num == 0:
			st.error("No subjects entered.")
			return

		percentage = total / num
		grade = grade_from_percent(percentage)

		st.subheader("Result")
		st.write(f"**Total Obtained:** {total:.2f} / {num * 100}")
		st.write(f"**Percentage:** {percentage:.2f}%")
		st.write(f"**Grade:** {grade}")

		# small visual indicator
		st.progress(min(100, max(0, int(percentage))))

	if st.button("Reset"):
		# reset all mark inputs by setting session state values to 0
		for i in range(1, int(subjects) + 1):
			key = f"mark_{i}"
			st.session_state[key] = 0.0


if __name__ == "__main__":
	main()
