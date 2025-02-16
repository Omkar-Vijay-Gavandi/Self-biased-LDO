import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the CSV file path for NMOS Ft vs gm/Id
file_path = r"D:\Desktop\PE\Techplots_45nm\Techplots_45nm\NMOS_tp_45nm\ft.csv"

try:
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Check if there are at least two columns
    if data.shape[1] < 2:
        print("The CSV file must contain at least two columns.")
    else:
        # Determine the number of column pairs
        num_pairs = data.shape[1] // 2

        # Generate corresponding lengths dynamically (from 45 nm to 4050 nm)
        start_length = 45  # nm
        step_size = 22.5   # nm
        lengths = np.arange(start_length, start_length + num_pairs * step_size, step_size)

        fig, ax = plt.subplots(figsize=(10, 7))

        # Store plotted lines for interactivity
        lines = []
        line_labels = {}

        # Loop through each pair of columns and plot the curves
        for i in range(num_pairs):
            x = data.iloc[:, 2 * i]      # gm/Id (X-axis)
            y = data.iloc[:, 2 * i + 1]  # Ft (Y-axis)

            # Extract the length from the predefined list
            length_nm = lengths[i]

            # Plot the curve and store the reference
            line, = ax.plot(x, y, linestyle='-')
            lines.append(line)
            line_labels[line] = f"l_nmos = {length_nm:.1f} nm"

        # Add plot labels and grid
        ax.set_title("NMOS: Ft vs gm/Id for Different Lengths")
        ax.set_xlabel("gm/Id")
        ax.set_ylabel("Ft (GHz)")
        ax.grid(True)

        # Annotation for hover effect
        annot = ax.annotate("", xy=(0, 0), xytext=(15, 15), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)

        # Function to update the annotation
        def update_annot(line, event):
            xdata, ydata = line.get_xdata(), line.get_ydata()
            ind = np.argmin(np.abs(xdata - event.xdata))  # Find closest x value
            annot.xy = (xdata[ind], ydata[ind])
            annot.set_text(line_labels[line])
            annot.set_visible(True)
            fig.canvas.draw_idle()

        # Event handler for mouse movement
        def on_hover(event):
            vis = annot.get_visible()
            if event.inaxes == ax:
                for line in lines:
                    if line.contains(event)[0]:  # Check if cursor is on a line
                        update_annot(line, event)
                        return
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

        # Connect the hover event
        fig.canvas.mpl_connect("motion_notify_event", on_hover)

        plt.show()

except FileNotFoundError:
    print("The specified file was not found. Please check the path and try again.")
except pd.errors.EmptyDataError:
    print("The file is empty. Please provide a valid CSV file.")
except Exception as e:
    print(f"An error occurred: {e}")
