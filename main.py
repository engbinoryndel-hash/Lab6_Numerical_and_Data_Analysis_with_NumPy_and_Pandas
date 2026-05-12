{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7eb9c4ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting numpy\n",
      "  Downloading numpy-2.4.4-cp314-cp314-win_amd64.whl.metadata (6.6 kB)\n",
      "Downloading numpy-2.4.4-cp314-cp314-win_amd64.whl (12.4 MB)\n",
      "   ---------------------------------------- 0.0/12.4 MB ? eta -:--:--\n",
      "   ---------- ----------------------------- 3.4/12.4 MB 25.0 MB/s eta 0:00:01\n",
      "   ---------------------------------------  12.3/12.4 MB 37.4 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 12.4/12.4 MB 31.5 MB/s  0:00:00\n",
      "Installing collected packages: numpy\n",
      "Successfully installed numpy-2.4.4\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.3 -> 26.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6e6e5429",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years of Experience: [ 1  3  5  7 10]\n",
      "Salary Matrix:\n",
      " [[ 50  60  70]\n",
      " [ 80  90 100]]\n",
      "Zeros Array:\n",
      " [[0. 0.]\n",
      " [0. 0.]]\n",
      "Ones Array:\n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Step 1: Import NumPy\n",
    "import numpy as np\n",
    "\n",
    "# Step 2: Create a 1D array representing years of experience\n",
    "years_exp = np.array([1, 3, 5, 7, 10])\n",
    "print(\"Years of Experience:\", years_exp)\n",
    "\n",
    "# Step 3: Create a 2D array representing sample salaries (in thousands)\n",
    "salaries = np.array([[50, 60, 70], [80, 90, 100]])\n",
    "print(\"Salary Matrix:\\n\", salaries)\n",
    "\n",
    "# Step 4: Create an array of zeros and ones for placeholder analysis\n",
    "zeros_array = np.zeros((2, 2)) # 2x2 zeros\n",
    "ones_array = np.ones((2, 3)) # 2x3 ones\n",
    "print(\"Zeros Array:\\n\", zeros_array)\n",
    "print(\"Ones Array:\\n\", ones_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b32c1451",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years of Experience: [ 1  3  5  7 10 12 15]\n",
      "\n",
      "Salary Matrix:\n",
      " [[ 50  60  70]\n",
      " [ 80  90 100]\n",
      " [110 120 130]\n",
      " [140 150 160]]\n",
      "\n",
      "Zeros Array:\n",
      " [[0. 0.]\n",
      " [0. 0.]]\n",
      "\n",
      "Ones Array:\n",
      " [[1. 1. 1.]\n",
      " [1. 1. 1.]]\n",
      "\n",
      "3x3 Identity Matrix:\n",
      " [[1. 0. 0.]\n",
      " [0. 1. 0.]\n",
      " [0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Step 1: Import NumPy\n",
    "# (Ensure you've installed it via %pip install numpy if you're still seeing the error!)\n",
    "\n",
    "# Step 2: Create a 1D array representing years of experience (Added 2 points: 12, 15)\n",
    "years_exp = np.array([1, 3, 5, 7, 10, 12, 15])\n",
    "print(\"Years of Experience:\", years_exp)\n",
    "\n",
    "# Step 3: Create a 2D array representing sample salaries (Added 2 rows for the new experience levels)\n",
    "# A 2D array must have consistent shapes; I've added two new lists of 3 values each.\n",
    "salaries = np.array([\n",
    "    [50, 60, 70], \n",
    "    [80, 90, 100],\n",
    "    [110, 120, 130], # New data point 1\n",
    "    [140, 150, 160]  # New data point 2\n",
    "])\n",
    "print(\"\\nSalary Matrix:\\n\", salaries)\n",
    "\n",
    "# Step 4: Create placeholder analysis arrays\n",
    "zeros_array = np.zeros((2, 2))\n",
    "ones_array = np.ones((2, 3))\n",
    "print(\"\\nZeros Array:\\n\", zeros_array)\n",
    "print(\"\\nOnes Array:\\n\", ones_array)\n",
    "\n",
    "# Step 5: Create a 3x3 identity matrix\n",
    "# The identity matrix has 1s on the diagonal and 0s elsewhere.\n",
    "identity_matrix = np.eye(3)\n",
    "print(\"\\n3x3 Identity Matrix:\\n\", identity_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "775ebc16",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years + 5: [ 6  8 10 12 15]\n",
      "Years * 2: [ 2  6 10 14 20]\n",
      "Dot Product: 32\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Element-wise addition\n",
    "exp_plus_5 = years_exp + 5 # Add 5 years to all experience values\n",
    "print(\"Years + 5:\", exp_plus_5)\n",
    "\n",
    "# Step 2: Element-wise multiplication\n",
    "exp_times_2 = years_exp * 2 # Multiply all values by 2\n",
    "print(\"Years * 2:\", exp_times_2)\n",
    "\n",
    "# Step 3: Dot product (simulate salary projections)\n",
    "sample1 = np.array([1, 2, 3])\n",
    "sample2 = np.array([4, 5, 6])\n",
    "dot_result = np.dot(sample1, sample2)\n",
    "print(\"Dot Product:\", dot_result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "25e5083c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years - 2: [-1  1  3  5  8 10 13]\n",
      "Years in Decades: [0.1 0.3 0.5 0.7 1.  1.2 1.5]\n",
      "\n",
      "Exponential (e^x) of sample1: [ 2.71828183  7.3890561  20.08553692]\n",
      "Natural Log (ln) of years_exp:\n",
      " [0.         1.09861229 1.60943791 1.94591015 2.30258509 2.48490665\n",
      " 2.7080502 ]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Re-establishing the arrays from the previous step\n",
    "years_exp = np.array([1, 3, 5, 7, 10, 12, 15])\n",
    "sample1 = np.array([1, 2, 3])\n",
    "\n",
    "# --- Experimenting with Subtraction and Division ---\n",
    "\n",
    "# Step 1: Element-wise subtraction (e.g., subtracting a 2-year gap)\n",
    "exp_minus_2 = years_exp - 2\n",
    "print(\"Years - 2:\", exp_minus_2)\n",
    "\n",
    "# Step 2: Element-wise division (e.g., converting to decades)\n",
    "exp_divided_10 = years_exp / 10\n",
    "print(\"Years in Decades:\", exp_divided_10)\n",
    "\n",
    "# --- Applying Mathematical Functions ---\n",
    "\n",
    "# Step 3: np.exp() - Calculates e^x for each element\n",
    "# This is often used in growth modeling or calculating softmax scores.\n",
    "exp_values = np.exp(sample1) \n",
    "print(\"\\nExponential (e^x) of sample1:\", exp_values)\n",
    "\n",
    "# Step 4: np.log() - Calculates the Natural Log (ln)\n",
    "# Note: np.log is the natural log; use np.log10 for base-10.\n",
    "log_values = np.log(years_exp)\n",
    "print(\"Natural Log (ln) of years_exp:\\n\", log_values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9be7da3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First year of experience: 1\n",
      "First two salaries: [50 60]\n",
      "Second column salaries: [60 90]\n",
      "Last year of experience: 10\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Access individual element\n",
    "print(\"First year of experience:\", years_exp[0])\n",
    "\n",
    "# Step 2: Slice arrays\n",
    "print(\"First two salaries:\", salaries[0, :2]) # First two elements of first row\n",
    "\n",
    "# Step 3: Access all rows for a specific column\n",
    "print(\"Second column salaries:\", salaries[:, 1])\n",
    "# Step 4: Negative indexing\n",
    "print(\"Last year of experience:\", years_exp[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "240ff554",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed Years: [15 12 10  7  5  3  1]\n",
      "\n",
      "Salaries (Rows Reversed):\n",
      " [[140 150 160]\n",
      " [110 120 130]\n",
      " [ 80  90 100]\n",
      " [ 50  60  70]]\n",
      "\n",
      "Subgroup (Middle 2x2 block):\n",
      " [[ 90 100]\n",
      " [120 130]]\n",
      "\n",
      "First two rows only:\n",
      " [[ 50  60  70]\n",
      " [ 80  90 100]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Data from previous steps\n",
    "years_exp = np.array([1, 3, 5, 7, 10, 12, 15])\n",
    "salaries = np.array([\n",
    "    [50, 60, 70], \n",
    "    [80, 90, 100],\n",
    "    [110, 120, 130],\n",
    "    [140, 150, 160]\n",
    "])\n",
    "\n",
    "# --- Reversing Arrays ---\n",
    "\n",
    "# Reverse 1D array: [start:stop:step] - a step of -1 goes backwards\n",
    "reversed_years = years_exp[::-1]\n",
    "print(\"Reversed Years:\", reversed_years)\n",
    "\n",
    "# Reverse 2D array rows (flips the matrix upside down)\n",
    "reversed_salaries_rows = salaries[::-1, :]\n",
    "print(\"\\nSalaries (Rows Reversed):\\n\", reversed_salaries_rows)\n",
    "\n",
    "\n",
    "# --- Slicing 2D Subgroups ---\n",
    "\n",
    "# Example: Get the middle section (Rows 1 & 2, Columns 1 & 2)\n",
    "# Remember: Slicing is [inclusive : exclusive]\n",
    "subgroup = salaries[1:3, 1:3] \n",
    "print(\"\\nSubgroup (Middle 2x2 block):\\n\", subgroup)\n",
    "\n",
    "# Example: Get the first two rows, all columns\n",
    "first_two_rows = salaries[:2, :]\n",
    "print(\"\\nFirst two rows only:\\n\", first_two_rows)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0b799ac7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reshaped Experience Array:\n",
      " [[1 2 3]\n",
      " [4 5 6]]\n",
      "Flattened Array: [1 2 3 4 5 6]\n",
      "Transposed Array:\n",
      " [[1 4]\n",
      " [2 5]\n",
      " [3 6]]\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Reshape 1D array into 2x3 matrix for batch analysis\n",
    "reshaped_exp = np.reshape(np.arange(1, 7), (2, 3))\n",
    "print(\"Reshaped Experience Array:\\n\", reshaped_exp)\n",
    "\n",
    "# Step 2: Flatten 2D arrays back into 1D\n",
    "flattened_exp = reshaped_exp.flatten()\n",
    "print(\"Flattened Array:\", flattened_exp)\n",
    "\n",
    "# Step 3: Transpose example\n",
    "print(\"Transposed Array:\\n\", reshaped_exp.T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "880bbdda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Data (1x12): [ 1  2  3  4  5  6  7  8  9 10 11 12]\n",
      "\n",
      "3x4 Matrix:\n",
      " [[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]]\n",
      "\n",
      "6x2 Matrix (using -1):\n",
      " [[ 1  2]\n",
      " [ 3  4]\n",
      " [ 5  6]\n",
      " [ 7  8]\n",
      " [ 9 10]\n",
      " [11 12]]\n",
      "\n",
      "3D Array (Tensor):\n",
      " [[[ 1  2]\n",
      "  [ 3  4]\n",
      "  [ 5  6]]\n",
      "\n",
      " [[ 7  8]\n",
      "  [ 9 10]\n",
      "  [11 12]]]\n",
      "\n",
      "Transposed (now 4x3):\n",
      " [[ 1  5  9]\n",
      " [ 2  6 10]\n",
      " [ 3  7 11]\n",
      " [ 4  8 12]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Creating a dataset of 12 elements (representing 12 samples or data points)\n",
    "data = np.arange(1, 13)\n",
    "print(\"Original Data (1x12):\", data)\n",
    "\n",
    "# --- 1. Reshape into 3x4 (3 samples with 4 features each) ---\n",
    "matrix_3x4 = data.reshape(3, 4)\n",
    "print(\"\\n3x4 Matrix:\\n\", matrix_3x4)\n",
    "\n",
    "# --- 2. The \"-1\" Trick (Automatic Dimension Calculation) ---\n",
    "# If you know you want 6 rows but don't want to do the math for columns, use -1.\n",
    "# NumPy will automatically calculate that 12 / 6 = 2 columns.\n",
    "auto_reshaped = data.reshape(6, -1)\n",
    "print(\"\\n6x2 Matrix (using -1):\\n\", auto_reshaped)\n",
    "\n",
    "# --- 3. 3D Reshaping (Modeling for Time-Series or RGB Images) ---\n",
    "# Reshape into (2 sheets, 3 rows, 2 columns)\n",
    "# This is how you represent batches of data.\n",
    "tensor_3d = data.reshape(2, 3, 2)\n",
    "print(\"\\n3D Array (Tensor):\\n\", tensor_3d)\n",
    "\n",
    "# --- 4. Transposing for Matrix Multiplication ---\n",
    "# Switching rows and columns of our 3x4 matrix to make it 4x3\n",
    "transposed_data = matrix_3x4.T\n",
    "print(\"\\nTransposed (now 4x3):\\n\", transposed_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c49830df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salaries after bonus:\n",
      " [[ 55  70  85]\n",
      " [ 85 100 115]]\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Add a bonus array to salaries using broadcasting\n",
    "bonus = np.array([5, 10, 15])\n",
    "salaries_with_bonus = salaries + bonus # Adds corresponding bonus to each column\n",
    "print(\"Salaries after bonus:\\n\", salaries_with_bonus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a7bf74eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Salaries (First Row): [50 60 70]\n",
      "Scaled Salaries (10% increase):\n",
      "[[ 55.  66.  77.]\n",
      " [ 88.  99. 110.]\n",
      " [121. 132. 143.]\n",
      " [154. 165. 176.]]\n",
      "\n",
      "Department-Specific Scaling:\n",
      "[[ 52.5  66.   84. ]\n",
      " [ 84.   99.  120. ]\n",
      " [115.5 132.  156. ]\n",
      " [147.  165.  192. ]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Original salaries matrix (4 rows, 3 columns)\n",
    "salaries = np.array([\n",
    "    [50, 60, 70], \n",
    "    [80, 90, 100],\n",
    "    [110, 120, 130],\n",
    "    [140, 150, 160]\n",
    "])\n",
    "\n",
    "# --- Scaling with a Scalar ---\n",
    "scaling_factor = 1.1\n",
    "scaled_salaries = salaries * scaling_factor\n",
    "\n",
    "print(\"Original Salaries (First Row):\", salaries[0])\n",
    "print(\"Scaled Salaries (10% increase):\")\n",
    "print(scaled_salaries)\n",
    "\n",
    "# --- Scaling with an Array (Column-wise) ---\n",
    "# Suppose each column represents a different department with different growth rates\n",
    "dept_growth = np.array([1.05, 1.10, 1.20]) # 5%, 10%, and 20% growth\n",
    "dept_scaled = salaries * dept_growth\n",
    "\n",
    "print(\"\\nDepartment-Specific Scaling:\")\n",
    "print(dept_scaled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "84d67a47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean experience: 7.571428571428571\n",
      "Std deviation of experience: 4.655477353371521\n",
      "Max salary: 160 Min salary: 50\n",
      "Sum of all salaries: 1260\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Mean of years of experience\n",
    "print(\"Mean experience:\", np.mean(years_exp))\n",
    "\n",
    "# Step 2: Standard deviation of experience\n",
    "print(\"Std deviation of experience:\", np.std(years_exp))\n",
    "\n",
    "# Step 3: Max and Min salaries\n",
    "print(\"Max salary:\", np.max(salaries), \"Min salary:\", np.min(salaries))\n",
    "\n",
    "# Step 4: Sum of salaries\n",
    "print(\"Sum of all salaries:\", np.sum(salaries))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8c65a6b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Median experience: 7.0\n",
      "25th Percentile: 4.0\n",
      "75th Percentile: 11.0\n",
      "\n",
      "Median salary per column (Dept): [ 95. 105. 115.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Using the data from our previous steps\n",
    "years_exp = np.array([1, 3, 5, 7, 10, 12, 15])\n",
    "salaries = np.array([\n",
    "    [50, 60, 70], \n",
    "    [80, 90, 100],\n",
    "    [110, 120, 130],\n",
    "    [140, 150, 160]\n",
    "])\n",
    "\n",
    "# --- 1. Compute the Median ---\n",
    "# The middle value when the data is sorted. \n",
    "# Unlike the mean, it isn't pulled away by extreme outliers.\n",
    "median_exp = np.median(years_exp)\n",
    "print(\"Median experience:\", median_exp)\n",
    "\n",
    "# --- 2. Compute Percentiles ---\n",
    "# The 25th percentile (Q1) is the value below which 25% of the data falls.\n",
    "# The 75th percentile (Q3) is the value below which 75% of the data falls.\n",
    "p25 = np.percentile(years_exp, 25)\n",
    "p75 = np.percentile(years_exp, 75)\n",
    "\n",
    "print(f\"25th Percentile: {p25}\")\n",
    "print(f\"75th Percentile: {p75}\")\n",
    "\n",
    "# --- 3. Median and Percentiles on 2D Arrays ---\n",
    "# You can calculate these for the whole matrix, or along a specific axis.\n",
    "# Axis 0 = column-wise, Axis 1 = row-wise\n",
    "median_salary_cols = np.median(salaries, axis=0)\n",
    "print(\"\\nMedian salary per column (Dept):\", median_salary_cols)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8a44f042",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sine of angles: [0.         0.70710678 1.        ]\n",
      "Cosine of angles: [1.00000000e+00 7.07106781e-01 6.12323400e-17]\n",
      "Sum of Salaries per person: [180 270 360 450]\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Apply trigonometric functions\n",
    "angles = np.array([0, np.pi/4, np.pi/2])\n",
    "print(\"Sine of angles:\", np.sin(angles))\n",
    "print(\"Cosine of angles:\", np.cos(angles))\n",
    "\n",
    "# Step 2: Apply function along rows (sum salaries per person)\n",
    "salary_sums = np.apply_along_axis(np.sum, 1, salaries)\n",
    "print(\"Sum of Salaries per person:\", salary_sums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b0cfe8cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square Root of Experience: [1.         1.73205081 2.23606798 2.64575131 3.16227766 3.46410162\n",
      " 3.87298335]\n",
      "\n",
      "Log-transformed Salaries (first row): [3.91202301 4.09434456 4.24849524]\n",
      "\n",
      "Adjusted Salaries (Custom Logic Applied per Row):\n",
      "[[ 52.5  63.   73.5]\n",
      " [ 84.   94.5 105. ]\n",
      " [121.  132.  143. ]\n",
      " [154.  165.  176. ]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Data from previous steps\n",
    "years_exp = np.array([1, 3, 5, 7, 10, 12, 15])\n",
    "salaries = np.array([\n",
    "    [50, 60, 70], \n",
    "    [80, 90, 100],\n",
    "    [110, 120, 130],\n",
    "    [140, 150, 160]\n",
    "])\n",
    "\n",
    "# --- 1. Math Transformations ---\n",
    "\n",
    "# Square Root: Useful for certain statistical calculations\n",
    "sqrt_exp = np.sqrt(years_exp)\n",
    "print(\"Square Root of Experience:\", sqrt_exp)\n",
    "\n",
    "# Natural Log: Often used to reduce the skewness of salary data\n",
    "log_salaries = np.log(salaries)\n",
    "print(\"\\nLog-transformed Salaries (first row):\", log_salaries[0])\n",
    "\n",
    "\n",
    "# --- 2. Custom Functions with np.apply_along_axis ---\n",
    "\n",
    "# Let's define a custom function: Calculate a \"Performance Adjusted Salary\"\n",
    "# If the average salary in the row is > 100, give a 10% bonus, else 5%\n",
    "def calculate_bonus_logic(row):\n",
    "    avg = np.mean(row)\n",
    "    if avg > 100:\n",
    "        return row * 1.10\n",
    "    else:\n",
    "        return row * 1.05\n",
    "\n",
    "# Apply along axis 1 (rows)\n",
    "# Syntax: (function, axis, array)\n",
    "adjusted_salaries = np.apply_along_axis(calculate_bonus_logic, 1, salaries)\n",
    "\n",
    "print(\"\\nAdjusted Salaries (Custom Logic Applied per Row):\")\n",
    "print(adjusted_salaries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e852331c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pandas\n",
      "  Downloading pandas-3.0.2-cp314-cp314-win_amd64.whl.metadata (19 kB)\n",
      "Requirement already satisfied: numpy>=2.3.3 in d:\\vscode files\\javier\\lab6_numerical and data analysis with numpy and pandas\\.venv\\lib\\site-packages (from pandas) (2.4.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in d:\\vscode files\\javier\\lab6_numerical and data analysis with numpy and pandas\\.venv\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Collecting tzdata (from pandas)\n",
      "  Downloading tzdata-2026.2-py2.py3-none-any.whl.metadata (1.4 kB)\n",
      "Requirement already satisfied: six>=1.5 in d:\\vscode files\\javier\\lab6_numerical and data analysis with numpy and pandas\\.venv\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Downloading pandas-3.0.2-cp314-cp314-win_amd64.whl (9.9 MB)\n",
      "   ---------------------------------------- 0.0/9.9 MB ? eta -:--:--\n",
      "   ---------------------------- ----------- 7.1/9.9 MB 60.5 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 9.9/9.9 MB 54.6 MB/s  0:00:00\n",
      "Downloading tzdata-2026.2-py2.py3-none-any.whl (349 kB)\n",
      "Installing collected packages: tzdata, pandas\n",
      "\n",
      "   ---------------------------------------- 0/2 [tzdata]\n",
      "   ---------------------------------------- 0/2 [tzdata]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   -------------------- ------------------- 1/2 [pandas]\n",
      "   ---------------------------------------- 2/2 [pandas]\n",
      "\n",
      "Successfully installed pandas-3.0.2 tzdata-2026.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.3 -> 26.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "19d261cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generated Data:\n",
      "     X   Y   Z\n",
      "0  21  26   6\n",
      "1  29  46  32\n",
      "2  47  44  32\n",
      "3  21  30  30\n",
      "4  28  32  22\n",
      "DataFrame with NumPy Transformations:\n",
      "     X   Y   Z     Log_X    Sqrt_Y\n",
      "0  21  26   6  3.044522  5.099020\n",
      "1  29  46  32  3.367296  6.782330\n",
      "2  47  44  32  3.850148  6.633250\n",
      "3  21  30  30  3.044522  5.477226\n",
      "4  28  32  22  3.332205  5.656854\n",
      "Correlation Matrix:\n",
      "                X         Y         Z     Log_X    Sqrt_Y\n",
      "X       1.000000  0.731630  0.512288  0.992670  0.736603\n",
      "Y       0.731630  1.000000  0.754296  0.776233  0.999523\n",
      "Z       0.512288  0.754296  1.000000  0.539498  0.769117\n",
      "Log_X   0.992670  0.776233  0.539498  1.000000  0.782068\n",
      "Sqrt_Y  0.736603  0.999523  0.769117  0.782068  1.000000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Step 1: Create a NumPy array of random data\n",
    "data = np.random.randint(1, 50, size=(5, 3))\n",
    "\n",
    "# Step 2: Convert the array into a DataFrame\n",
    "df_data = pd.DataFrame(data, columns=['X', 'Y', 'Z'])\n",
    "print(\"Generated Data:\\n\", df_data)\n",
    "\n",
    "# Step 3: Apply NumPy functions to DataFrame columns\n",
    "df_data['Log_X'] = np.log(df_data['X'])\n",
    "df_data['Sqrt_Y'] = np.sqrt(df_data['Y'])\n",
    "print(\"DataFrame with NumPy Transformations:\\n\", df_data)\n",
    "\n",
    "# Step 4: Analyze data using Pandas correlation\n",
    "print(\"Correlation Matrix:\\n\", df_data.corr())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f8e12307",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generated Data:\n",
      "     X   Y   Z\n",
      "0  22  21  18\n",
      "1  48  15  29\n",
      "2  46  29  39\n",
      "3  14  27  19\n",
      "4  33  36  41\n",
      "\n",
      "--- Statistics ---\n",
      "Mean of each column:\n",
      " X    32.6\n",
      "Y    25.6\n",
      "Z    29.2\n",
      "dtype: float64\n",
      "Median of each column:\n",
      " [33. 27. 29.]\n",
      "\n",
      "Updated DataFrame with New Transformations:\n",
      "    X   Y   Z  Square_Z         Exp_X     Log_X    Sqrt_Y\n",
      "0  22  21  18       324  3.584913e+09  3.091042  4.582576\n",
      "1  48  15  29       841  7.016736e+20  3.871201  3.872983\n",
      "2  46  29  39      1521  9.496119e+19  3.828641  5.385165\n",
      "3  14  27  19       361  1.202604e+06  2.639057  5.196152\n",
      "4  33  36  41      1681  2.146436e+14  3.496508  6.000000\n",
      "\n",
      "Correlation Matrix:\n",
      "                  X         Y         Z  Square_Z     Exp_X     Log_X    Sqrt_Y\n",
      "X         1.000000 -0.192129  0.692063  0.635334  0.667207  0.987121 -0.229623\n",
      "Y        -0.192129  1.000000  0.567350  0.629024 -0.727841 -0.130666  0.997641\n",
      "Z         0.692063  0.567350  1.000000  0.996289  0.059905  0.732108  0.528299\n",
      "Square_Z  0.635334  0.629024  0.996289  1.000000 -0.024147  0.683593  0.592452\n",
      "Exp_X     0.667207 -0.727841  0.059905 -0.024147  1.000000  0.600008 -0.765811\n",
      "Log_X     0.987121 -0.130666  0.732108  0.683593  0.600008  1.000000 -0.170894\n",
      "Sqrt_Y   -0.229623  0.997641  0.528299  0.592452 -0.765811 -0.170894  1.000000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Step 1: Create a NumPy array of random data\n",
    "data = np.random.randint(1, 50, size=(5, 3))\n",
    "\n",
    "# Step 2: Convert the array into a DataFrame\n",
    "df_data = pd.DataFrame(data, columns=['X', 'Y', 'Z'])\n",
    "print(\"Generated Data:\\n\", df_data)\n",
    "\n",
    "# --- Step 3: Compute Overall Column Statistics ---\n",
    "# We can use NumPy functions on the entire DataFrame or specific columns\n",
    "print(\"\\n--- Statistics ---\")\n",
    "print(\"Mean of each column:\\n\", np.mean(df_data, axis=0))\n",
    "print(\"Median of each column:\\n\", np.median(df_data, axis=0))\n",
    "\n",
    "# --- Step 4: Apply Additional Transformations ---\n",
    "# Square the values in column Z\n",
    "df_data['Square_Z'] = np.square(df_data['Z'])\n",
    "\n",
    "# Calculate the exponential of column X (e^x)\n",
    "# Note: Values grow very large quickly!\n",
    "df_data['Exp_X'] = np.exp(df_data['X'])\n",
    "\n",
    "# Apply original transformations\n",
    "df_data['Log_X'] = np.log(df_data['X'])\n",
    "df_data['Sqrt_Y'] = np.sqrt(df_data['Y'])\n",
    "\n",
    "print(\"\\nUpdated DataFrame with New Transformations:\")\n",
    "print(df_data)\n",
    "\n",
    "# Step 5: Analyze data using Pandas correlation\n",
    "print(\"\\nCorrelation Matrix:\\n\", df_data.corr())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "45332583",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data saved to 'sample_data.csv'.\n",
      "Imported DataFrame:\n",
      "     X   Y   Z  Square_Z         Exp_X     Log_X    Sqrt_Y\n",
      "0  22  21  18       324  3.584913e+09  3.091042  4.582576\n",
      "1  48  15  29       841  7.016736e+20  3.871201  3.872983\n",
      "2  46  29  39      1521  9.496119e+19  3.828641  5.385165\n",
      "3  14  27  19       361  1.202604e+06  2.639057  5.196152\n",
      "4  33  36  41      1681  2.146436e+14  3.496508  6.000000\n",
      "Summary Statistics:\n",
      "               X         Y         Z     Square_Z         Exp_X     Log_X  \\\n",
      "count   5.00000   5.00000   5.00000     5.000000  5.000000e+00  5.000000   \n",
      "mean   32.60000  25.60000  29.20000   945.600000  1.593270e+20  3.385290   \n",
      "std    14.79189   7.98749  10.77961   634.622565  3.059567e+20  0.521652   \n",
      "min    14.00000  15.00000  18.00000   324.000000  1.202604e+06  2.639057   \n",
      "25%    22.00000  21.00000  19.00000   361.000000  3.584913e+09  3.091042   \n",
      "50%    33.00000  27.00000  29.00000   841.000000  2.146436e+14  3.496508   \n",
      "75%    46.00000  29.00000  39.00000  1521.000000  9.496119e+19  3.828641   \n",
      "max    48.00000  36.00000  41.00000  1681.000000  7.016736e+20  3.871201   \n",
      "\n",
      "         Sqrt_Y  \n",
      "count  5.000000  \n",
      "mean   5.007375  \n",
      "std    0.811013  \n",
      "min    3.872983  \n",
      "25%    4.582576  \n",
      "50%    5.196152  \n",
      "75%    5.385165  \n",
      "max    6.000000  \n",
      "Column Means:\n",
      " X           3.260000e+01\n",
      "Y           2.560000e+01\n",
      "Z           2.920000e+01\n",
      "Square_Z    9.456000e+02\n",
      "Exp_X       1.593270e+20\n",
      "Log_X       3.385290e+00\n",
      "Sqrt_Y      5.007375e+00\n",
      "dtype: float64\n",
      "Column Standard Deviations:\n",
      " X           1.479189e+01\n",
      "Y           7.987490e+00\n",
      "Z           1.077961e+01\n",
      "Square_Z    6.346226e+02\n",
      "Exp_X       3.059567e+20\n",
      "Log_X       5.216522e-01\n",
      "Sqrt_Y      8.110125e-01\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Save the DataFrame to a CSV file\n",
    "df_data.to_csv('sample_data.csv', index=False)\n",
    "print(\"Data saved to 'sample_data.csv'.\")\n",
    "\n",
    "# Step 2: Load the CSV file back into a new DataFrame\n",
    "df_imported = pd.read_csv('sample_data.csv')\n",
    "print(\"Imported DataFrame:\\n\", df_imported)\n",
    "\n",
    "# Step 3: Generate summary statistics\n",
    "summary_stats = df_imported.describe()\n",
    "print(\"Summary Statistics:\\n\", summary_stats)\n",
    "\n",
    "# Step 4: Display column means and standard deviations\n",
    "print(\"Column Means:\\n\", df_imported.mean())\n",
    "print(\"Column Standard Deviations:\\n\", df_imported.std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0f706df3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Initial data saved to 'sample_data.csv'.\n",
      "\n",
      "Imported DataFrame with New Columns:\n",
      "     X   Y   Z  Square_Z         Exp_X     Log_X    Sqrt_Y  Sum_XY   Z_per_X\n",
      "0  22  21  18       324  3.584913e+09  3.091042  4.582576      43  0.818182\n",
      "1  48  15  29       841  7.016736e+20  3.871201  3.872983      63  0.604167\n",
      "2  46  29  39      1521  9.496119e+19  3.828641  5.385165      75  0.847826\n",
      "3  14  27  19       361  1.202604e+06  2.639057  5.196152      41  1.357143\n",
      "4  33  36  41      1681  2.146436e+14  3.496508  6.000000      69  1.242424\n",
      "\n",
      "--- Summary Statistics ---\n",
      "              X         Y         Z     Square_Z         Exp_X     Log_X  \\\n",
      "count   5.00000   5.00000   5.00000     5.000000  5.000000e+00  5.000000   \n",
      "mean   32.60000  25.60000  29.20000   945.600000  1.593270e+20  3.385290   \n",
      "std    14.79189   7.98749  10.77961   634.622565  3.059567e+20  0.521652   \n",
      "min    14.00000  15.00000  18.00000   324.000000  1.202604e+06  2.639057   \n",
      "25%    22.00000  21.00000  19.00000   361.000000  3.584913e+09  3.091042   \n",
      "50%    33.00000  27.00000  29.00000   841.000000  2.146436e+14  3.496508   \n",
      "75%    46.00000  29.00000  39.00000  1521.000000  9.496119e+19  3.828641   \n",
      "max    48.00000  36.00000  41.00000  1681.000000  7.016736e+20  3.871201   \n",
      "\n",
      "         Sqrt_Y     Sum_XY   Z_per_X  \n",
      "count  5.000000   5.000000  5.000000  \n",
      "mean   5.007375  58.200000  0.973948  \n",
      "std    0.811013  15.401299  0.314573  \n",
      "min    3.872983  41.000000  0.604167  \n",
      "25%    4.582576  43.000000  0.818182  \n",
      "50%    5.196152  63.000000  0.847826  \n",
      "75%    5.385165  69.000000  1.242424  \n",
      "max    6.000000  75.000000  1.357143  \n",
      "\n",
      "Modified data successfully saved to 'modified_sample_data.csv'.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# --- Step 1: Initial Save ---\n",
    "# Assuming df_data exists from our previous steps\n",
    "df_data.to_csv('sample_data.csv', index=False)\n",
    "print(\"Initial data saved to 'sample_data.csv'.\")\n",
    "\n",
    "# --- Step 2: Import & Modify ---\n",
    "df_imported = pd.read_csv('sample_data.csv')\n",
    "\n",
    "# Adding a new calculated column: Sum of X and Y\n",
    "df_imported['Sum_XY'] = df_imported['X'] + df_imported['Y']\n",
    "\n",
    "# Adding another common metric: Ratio of Z to X\n",
    "df_imported['Z_per_X'] = df_imported['Z'] / df_imported['X']\n",
    "\n",
    "print(\"\\nImported DataFrame with New Columns:\\n\", df_imported.head())\n",
    "\n",
    "# --- Step 3: Statistics & Review ---\n",
    "print(\"\\n--- Summary Statistics ---\")\n",
    "print(df_imported.describe())\n",
    "\n",
    "# --- Step 4: Save Modified Data ---\n",
    "df_imported.to_csv('modified_sample_data.csv', index=False)\n",
    "print(\"\\nModified data successfully saved to 'modified_sample_data.csv'.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "e1bc9b79",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (818833942.py, line 4)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[48]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mEvaluation Copy 6\u001b[39m\n               ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Load the Stack Overflow 2023 Developer Survey dataset\n",
    "df_kaggle = pd.read_csv('survey_results_public.csv')\n",
    "print(\"Loaded Dataset:\\n\", df_kaggle.head())\n",
    "Evaluation Copy 6\n",
    "Strictly for TUP ECE students only\n",
    "# Step 2: Select relevant columns\n",
    "df_subset = df_kaggle[['Country', 'EdLevel', 'YearsCodePro', 'ConvertedComp']]\n",
    "print(\"Subset of Data:\\n\", df_subset.head())\n",
    "# Step 3: Clean the data by dropping rows with missing values\n",
    "df_clean = df_subset.dropna()\n",
    "print(\"Cleaned Data:\\n\", df_clean.head())\n",
    "# Step 4: Categorize experience into groups\n",
    "df_clean['ExperienceLevel'] = np.where(df_clean['YearsCodePro'] >= 10, 'Senior',\n",
    "'Junior')\n",
    "# Step 5: Group data by Country and ExperienceLevel, compute average salary\n",
    "grouped_data = df_clean.groupby(['Country',\n",
    "'ExperienceLevel'])['ConvertedComp'].mean()\n",
    "print(\"Grouped Average Salary:\\n\", grouped_data.head())\n",
    "# Step 6: Reset index for readability\n",
    "grouped_data = grouped_data.reset_index()\n",
    "print(\"Formatted Grouped Data:\\n\", grouped_data.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "54540336",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Japhet Javier's Array: [32 27  7 27 29 23 11 38  7 34]\n",
      "Mean: 23.5 Std Dev: 10.716809226630843\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 3505\n",
    "np.random.seed(STUDENT_ID)\n",
    "data = np.random.randint(1, STUDENT_ID % 100 + 50, size=10)\n",
    "print(f\"{STUDENT_NAME}'s Array:\", data)\n",
    "mean_val = np.mean(data)\n",
    "std_val = np.std(data)\n",
    "print(\"Mean:\", mean_val, \"Std Dev:\", std_val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "58997023",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Japhet Javier's Matrix:\n",
      " [[20 30 32 27]\n",
      " [14 14 10 25]\n",
      " [33 14  5 23]]\n",
      "Row sums: [109  63  75]\n",
      "Column sums: [67 58 47 75]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Ryndel Engbino\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "matrix = np.random.randint(1, STUDENT_ID % 50 + 20, size=(3,4))\n",
    "print(f\"{STUDENT_NAME}'s Matrix:\\n\", matrix)\n",
    "row_sums = np.sum(matrix, axis=1)\n",
    "col_sums = np.sum(matrix, axis=0)\n",
    "print(\"Row sums:\", row_sums)\n",
    "print(\"Column sums:\", col_sums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "7f704e62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Japhet Javier's 3D Array:\n",
      " [[[19 26 13]\n",
      "  [11 13 13]\n",
      "  [ 9 24  0]]\n",
      "\n",
      " [[13 14 22]\n",
      "  [17  9  4]\n",
      "  [22  6  2]]\n",
      "\n",
      " [[21 14  5]\n",
      "  [23  4 10]\n",
      "  [ 7 23  8]]]\n",
      "Slice[:,1,:]:\n",
      " [[11 13 13]\n",
      " [17  9  4]\n",
      " [23  4 10]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Ryndel Engbino\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "arr3d = np.random.randint(0, STUDENT_ID % 20 + 10, size=(3,3,3))\n",
    "print(f\"{STUDENT_NAME}'s 3D Array:\\n\", arr3d)\n",
    "slice_mid = arr3d[:,1,:]\n",
    "print(\"Slice[:,1,:]:\\n\", slice_mid)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "87a35dbf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Japhet Javier's Original: [20 64 27 44 10 25 42 23 35 47]\n",
      "Filtered subset: []\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Ryndel Engbino\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "x = np.random.randint(1, STUDENT_ID % 100 + 50, size=10)\n",
    "filtered = x[(x>STUDENT_ID%50) & (x<STUDENT_ID%100)]\n",
    "print(f\"{STUDENT_NAME}'s Original:\", x)\n",
    "print(\"Filtered subset:\", filtered)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "8319483c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix A:\n",
      " [[20 30]\n",
      " [32 27]]\n",
      "Matrix B:\n",
      " [[14 14]\n",
      " [10 25]]\n",
      "A @ B:\n",
      " [[ 580 1030]\n",
      " [ 718 1123]]\n",
      "Determinant of A: -419.99999999999994\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "A = np.random.randint(1, STUDENT_ID % 50 + 20, size=(2,2))\n",
    "B = np.random.randint(1, STUDENT_ID % 50 + 20, size=(2,2))\n",
    "print(\"Matrix A:\\n\", A)\n",
    "print(\"Matrix B:\\n\", B)\n",
    "product = A @ B\n",
    "det_A = np.linalg.det(A)\n",
    "print(\"A @ B:\\n\", product)\n",
    "print(\"Determinant of A:\", det_A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "c4a3c154",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Japhet Javier's Angles: [0.         0.8975979  1.7951958  2.6927937  3.5903916  4.48798951\n",
      " 5.38558741 6.28318531]\n",
      "Sine: [ 0.00000000e+00  7.81831482e-01  9.74927912e-01  4.33883739e-01\n",
      " -4.33883739e-01 -9.74927912e-01 -7.81831482e-01 -2.44929360e-16]\n",
      "Cosine: [ 1.          0.6234898  -0.22252093 -0.90096887 -0.90096887 -0.22252093\n",
      "  0.6234898   1.        ]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Ryndel Engbino\"\n",
    "STUDENT_ID = 1117\n",
    "angles = np.linspace(0, 2*np.pi, 8)\n",
    "sine_vals = np.sin(angles)\n",
    "cos_vals = np.cos(angles)\n",
    "print(f\"{STUDENT_NAME}'s Angles:\", angles)\n",
    "print(\"Sine:\", sine_vals)\n",
    "print(\"Cosine:\", cos_vals)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "9f5fa867",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Japhet Javier's Modified 4x4 Array:\n",
      " [[ 0 30  0 27]\n",
      " [14 14 10 25]\n",
      " [ 0 14  0 23]\n",
      " [ 7 35 22  5]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "arr = np.random.randint(1, STUDENT_ID % 50 + 20, size=(4,4))\n",
    "arr[::2, ::2] = 0\n",
    "print(f\"{STUDENT_NAME}'s Modified 4x4 Array:\\n\", arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "59c99a4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Japhet Javier's Scores: [19 63 26 43  9 24 41 22 34 46]\n",
      "Grades: ['Fail' 'Fail' 'Fail' 'Fail' 'Fail' 'Fail' 'Fail' 'Fail' 'Fail' 'Fail']\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "scores = np.random.randint(0, STUDENT_ID % 100 + 50, 10)\n",
    "grades = np.where(scores>=STUDENT_ID%70,'Pass','Fail')\n",
    "print(f\"{STUDENT_NAME}'s Scores:\", scores)\n",
    "print(\"Grades:\", grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "281cc890",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array:\n",
      " [[20 30 32 27]\n",
      " [14 14 10 25]\n",
      " [33 14  5 23]]\n",
      "Flattened: [20 30 32 27 14 14 10 25 33 14  5 23]\n",
      "Transposed:\n",
      " [[20 14 33]\n",
      " [30 14 14]\n",
      " [32 10  5]\n",
      " [27 25 23]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "arr = np.random.randint(1, STUDENT_ID % 50 + 20, size=(3,4))\n",
    "flat_arr = arr.flatten()\n",
    "transposed_arr = arr.T\n",
    "print(\"Original array:\\n\", arr)\n",
    "print(\"Flattened:\", flat_arr)\n",
    "print(\"Transposed:\\n\", transposed_arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "73d46c63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array with conditional replacements:\n",
      " [[-1 -1 -1]\n",
      " [27 -1 -1]\n",
      " [-1 25 33]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "arr = np.random.randint(1, STUDENT_ID % 50 + 20, (3,3))\n",
    "mask = arr % 2 == 0\n",
    "arr[mask] = -1\n",
    "print(\"Array with conditional replacements:\\n\", arr)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "45225e1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            Name  Score  YearsCodePro\n",
      "0  Japhet Javier     36            11\n",
      "1  Japhet Javier     46            13\n",
      "2  Japhet Javier     48            13\n",
      "3  Japhet Javier     43             9\n",
      "4  Japhet Javier     62            24\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "df = pd.DataFrame({\n",
    " 'Name': [STUDENT_NAME]*5,\n",
    " 'Score': np.random.randint(STUDENT_ID%50,\n",
    "STUDENT_ID%100+50,5),\n",
    " 'YearsCodePro': np.random.randint(0, STUDENT_ID%20+10,5)\n",
    "})\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "db65308f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EdLevel\n",
      "Bachelor     90425.0\n",
      "Master      142877.5\n",
      "PhD          57885.0\n",
      "Name: ConvertedComp, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "df = pd.DataFrame({\n",
    "'EdLevel': ['Bachelor','Master','PhD','Bachelor','Master'],\n",
    "# Corrected to use a functional salary range, e.g., 40000 to 150000\n",
    "'ConvertedComp': np.random.randint(40000, 150000, 5)\n",
    "})\n",
    "avg_salary = df.groupby('EdLevel')['ConvertedComp'].mean()\n",
    "print(avg_salary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "618a48af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Country  ConvertedComp\n",
      "1          USA         143487\n",
      "4      Germany         142268\n",
      "3       Canada         104351\n",
      "0  Philippines          76499\n",
      "2           UK          57885\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "df = pd.DataFrame({\n",
    " 'Country': ['Philippines','USA','UK','Canada','Germany'],\n",
    " 'ConvertedComp': np.random.randint(40000, 150000, 5)\n",
    "})\n",
    "top5 = df.sort_values(by='ConvertedComp', ascending=False)\n",
    "print(top5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "d76e53ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            Name  YearsCodePro\n",
      "0  Japhet Javier            19\n",
      "1  Japhet Javier            26\n",
      "2  Japhet Javier            13\n",
      "3  Japhet Javier            11\n",
      "4  Japhet Javier            13\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "df = pd.DataFrame({\n",
    " 'Name':[STUDENT_NAME]*5,\n",
    " 'YearsCodePro': np.random.randint(0, STUDENT_ID%20+10,5)\n",
    "})\n",
    "high_exp = df[df['YearsCodePro']>STUDENT_ID%10]\n",
    "print(high_exp)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "719e8fdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   ConvertedComp   Bracket\n",
      "0          76499   50-100k\n",
      "1         143487  100-150k\n",
      "2          57885   50-100k\n",
      "3         104351  100-150k\n",
      "4         142268  100-150k\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "df = pd.DataFrame({'ConvertedComp': np.random.randint(40000,\n",
    "150000, 5)})\n",
    "bins = [0, 50000, 100000, 150000, 200000]\n",
    "labels = ['0-50k', '50-100k', '100-150k', '>150k']\n",
    "df['Bracket'] = pd.cut(df['ConvertedComp'], bins=bins, labels=labels)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "e267d8e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   ConvertedComp    LogComp\n",
      "0          76499  11.245033\n",
      "1         143487  11.874000\n",
      "2          57885  10.966214\n",
      "3         104351  11.555515\n",
      "4         142268  11.865468\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "# Original Code Issue:\n",
    "# np.random.randint(STUDENT_ID%40000, STUDENT_ID%150000, 5)\n",
    "# -> np.random.randint(12345, 12345, 5) which is a zero-length range.\n",
    "# Corrected Code: Using a functional salary range (40000 to 150000)\n",
    "df = pd.DataFrame({'ConvertedComp': np.random.randint(40000,\n",
    "150000, 5)})\n",
    "df['LogComp'] = np.log(df['ConvertedComp'])\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "62ef48c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               YearsCodePro  ConvertedComp\n",
      "YearsCodePro       1.000000      -0.316679\n",
      "ConvertedComp     -0.316679       1.000000\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "df = pd.DataFrame({\n",
    "'YearsCodePro': np.random.randint(0, STUDENT_ID%20+10, 5),\n",
    "'ConvertedComp': np.random.randint(40000, 150000, 5)\n",
    "})\n",
    "corr_matrix = df.corr()\n",
    "print(corr_matrix)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "52449d9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    EdLevel      mean    median           std\n",
      "0  Bachelor   90425.0   90425.0  19694.338070\n",
      "1    Master  142877.5  142877.5    861.963166\n",
      "2       PhD   57885.0   57885.0           NaN\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "\n",
    "df = pd.DataFrame({\n",
    "    'EdLevel':['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],\n",
    "    'ConvertedComp': np.random.randint(40000, 150000, 5)\n",
    "})\n",
    "\n",
    "# FIX: Keep the assignment and the groupby logic on the same line (or use parentheses)\n",
    "summary = df.groupby('EdLevel')['ConvertedComp'].agg(['mean', 'median', 'std']).reset_index()\n",
    "\n",
    "print(summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "9832ce7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   ConvertedComp HighPay\n",
      "0          76499      No\n",
      "1         143487     Yes\n",
      "2          57885      No\n",
      "3         104351      No\n",
      "4         142268     Yes\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "# Generate salaries: [100727, 136195, 130612, 100727, 95233]\n",
    "df = pd.DataFrame({'ConvertedComp': np.random.randint(40000,\n",
    "150000, 5)})\n",
    "threshold = 110000\n",
    "# Create the 'HighPay' column using np.where()\n",
    "df['HighPay'] = np.where(df['ConvertedComp'] > threshold, 'Yes', 'No')\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "cee34d63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 mean     max\n",
      "Country                      \n",
      "Canada       104351.0  104351\n",
      "Germany      142268.0  142268\n",
      "Philippines   76499.0   76499\n",
      "UK            57885.0   57885\n",
      "USA          143487.0  143487\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "STUDENT_NAME = \"Japhet Javier\"\n",
    "STUDENT_ID = 1117\n",
    "np.random.seed(STUDENT_ID)\n",
    "\n",
    "df = pd.DataFrame({\n",
    "    'Country': ['Philippines', 'USA', 'UK', 'Canada', 'Germany'],\n",
    "    'ConvertedComp': np.random.randint(40000, 150000, 5)\n",
    "})\n",
    "\n",
    "# FIX: Move the code up to this line\n",
    "top_countries = df.groupby('Country')['ConvertedComp'].agg(['mean', 'max'])\n",
    "\n",
    "print(top_countries)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.14.2)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}