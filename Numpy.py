{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Prathap241801208/Machine-learning-using-AI/blob/main/Numpy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "5fd9a254",
      "metadata": {
        "id": "5fd9a254",
        "outputId": "10524dbd-6c84-48b4-eb26-c0dc4fae29a0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 2 3 4 5]\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "arr = np.array([1,2,3,4,5])\n",
        "print(arr)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8577a09a",
      "metadata": {
        "id": "8577a09a",
        "outputId": "64e3f86c-7c35-46d4-b1a3-271cae310108",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "42\n"
          ]
        }
      ],
      "source": [
        "arr = np.array(42)\n",
        "print(arr)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "identity_matrix = np.eye(3)\n",
        "print(identity_matrix)\n",
        "identity_matrix = np.eye(4)\n",
        "print(\"\\n\",identity_matrix)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VGvwkbwzsm9e",
        "outputId": "5bbae766-3f3f-4b00-ccda-145a998d0d08"
      },
      "id": "VGvwkbwzsm9e",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1. 0. 0.]\n",
            " [0. 1. 0.]\n",
            " [0. 0. 1.]]\n",
            "\n",
            " [[1. 0. 0. 0.]\n",
            " [0. 1. 0. 0.]\n",
            " [0. 0. 1. 0.]\n",
            " [0. 0. 0. 1.]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "a = np.array([1., 2., 3., 4.])\n",
        "b = np.array([5., 6., 7., 8.])\n",
        "\n",
        "print(a + b)\n",
        "print(a - b)\n",
        "print(a * b)\n",
        "print(a / b)\n",
        "print(a ** b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gIQMo7Uutvng",
        "outputId": "4e06f79c-979e-4c9d-daca-52b1dc11b3bf"
      },
      "id": "gIQMo7Uutvng",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[ 6.  8. 10. 12.]\n",
            "[-4. -4. -4. -4.]\n",
            "[ 5. 12. 21. 32.]\n",
            "[0.2        0.33333333 0.42857143 0.5       ]\n",
            "[1.0000e+00 6.4000e+01 2.1870e+03 6.5536e+04]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "zeros_arr = np.zeros((5,2))\n",
        "zeros_arr = np.zeros((5,))\n",
        "print(zeros_arr)\n",
        "zeros_arr = np.zeros((2,3))\n",
        "print(zeros_arr)\n",
        "print(\"Data type of the array: \",zeros_arr.dtype)\n",
        "zeros_arr_int = np.zeros((3,3), dtype=np.int16)\n",
        "print(\"\\nArray of zeros with integer elements: \\n\",zeros_arr_int)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eB246btCubSI",
        "outputId": "4efa17ee-8ede-4570-cc35-fb8b24f6c683"
      },
      "id": "eB246btCubSI",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0. 0. 0. 0. 0.]\n",
            "[[0. 0. 0.]\n",
            " [0. 0. 0.]]\n",
            "Data type of the array:  float64\n",
            "\n",
            "Array of zeros with integer elements: \n",
            " [[0 0 0]\n",
            " [0 0 0]\n",
            " [0 0 0]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "original_array = np.array([[10, 20], [30, 40]])\n",
        "print(\"Original array:\\n\", original_array)\n",
        "\n",
        "flattened_array = original_array.flatten()\n",
        "flattened_array[0] = 999\n",
        "print(\"Flattened array:\\n\", flattened_array)\n",
        "print(\"Original array:\\n\", original_array)\n",
        "\n",
        "raveled_array = original_array.ravel()\n",
        "raveled_array[1] = 888\n",
        "\n",
        "print(\"Raveled array:\\n\", raveled_array)\n",
        "print(\"Original array:\\n\", original_array)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ow6sxBGhvAu9",
        "outputId": "48ee1b58-d57f-45b6-a2e5-e4bfd9f1009b"
      },
      "id": "ow6sxBGhvAu9",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original array:\n",
            " [[10 20]\n",
            " [30 40]]\n",
            "Flattened array:\n",
            " [999  20  30  40]\n",
            "Original array:\n",
            " [[10 20]\n",
            " [30 40]]\n",
            "Raveled array:\n",
            " [ 10 888  30  40]\n",
            "Original array:\n",
            " [[ 10 888]\n",
            " [ 30  40]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "arr1 = np.array([[1, 2], [3, 4]])\n",
        "arr2 = np.array([[2, 1], [3, 5]])\n",
        "\n",
        "greater_than = arr1 > arr2\n",
        "less_than = arr1 < arr2\n",
        "equal_to = arr1 == arr2\n",
        "\n",
        "print(\"Greater than:\\n\", greater_than)\n",
        "print(\"\\nLess than:\\n\", less_than)\n",
        "print(\"\\nEqual to:\\n\", equal_to)\n",
        "\n",
        "arr3 = np.array([1, 2, 3])\n",
        "arr4 = np.array([1, 2, 3])\n",
        "arr5 = np.array([1, 2, 4])\n",
        "\n",
        "result1 = np.array_equal(arr3, arr4)\n",
        "result2 = np.array_equal(arr3, arr5)\n",
        "\n",
        "print(\"\\nArray-wise comparison 1:\", result1)\n",
        "print(\"Array-wise comparison 2:\", result2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1Gf6O9_Dve4Q",
        "outputId": "10664f7f-e634-4800-9cf0-92d1c76e4473"
      },
      "id": "1Gf6O9_Dve4Q",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Greater than:\n",
            " [[False  True]\n",
            " [False False]]\n",
            "\n",
            "Less than:\n",
            " [[ True False]\n",
            " [False  True]]\n",
            "\n",
            "Equal to:\n",
            " [[False False]\n",
            " [ True False]]\n",
            "\n",
            "Array-wise comparison 1: True\n",
            "Array-wise comparison 2: False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c7f04f12",
      "metadata": {
        "id": "c7f04f12",
        "outputId": "4e0f1169-6fe6-4efc-f0ac-b30703a4db3b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Size of each element of list in bytes: 48\n",
            "Size of each element of list in bytes: 48000\n",
            "Size of each element of the numpy array in bytes: 8\n",
            "Size of the whole Numpy array in bytes: 8000\n"
          ]
        }
      ],
      "source": [
        "import sys\n",
        "S = range(1000)\n",
        "print(\"Size of each element of list in bytes:\" ,sys.getsizeof(S))\n",
        "print(\"Size of each element of list in bytes:\",sys.getsizeof(S)*len(S))\n",
        "D=np.arange(1000)\n",
        "print(\"Size of each element of the numpy array in bytes:\",D.itemsize)\n",
        "print(\"Size of the whole Numpy array in bytes:\",D.size*D.itemsize)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])\n",
        "print(arr)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "guotca09lEr0",
        "outputId": "4bfb6ac1-a61a-4842-b8b9-8cca760fc7e5"
      },
      "id": "guotca09lEr0",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[1 2 3]\n",
            "  [4 5 6]]\n",
            "\n",
            " [[1 2 3]\n",
            "  [4 5 6]]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "zeros_arr = np.zeros((5,2))\n",
        "zeros_arr = np.zeros((5,))\n",
        "print(zeros_arr)\n",
        "zeros_arr = np.zeros((2,3))\n",
        "print(zeros_arr)\n",
        "print(\"Data type of the array: \",zeros_arr.dtype)\n",
        "zeros_arr_int = np.zeros((3,3), dtype=np.int16)\n",
        "print(\"\\nArray of zeros with integer elements: \\n\",zeros_arr_int)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7VjTa7pKmiNd",
        "outputId": "c4f57481-6282-410c-adb6-d7b949c492c6"
      },
      "id": "7VjTa7pKmiNd",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0. 0. 0. 0. 0.]\n",
            "[[0. 0. 0.]\n",
            " [0. 0. 0.]]\n",
            "Data type of the array:  float64\n",
            "\n",
            "Array of zeros with integer elements: \n",
            " [[0 0 0]\n",
            " [0 0 0]\n",
            " [0 0 0]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ones_arr = np.ones(6)\n",
        "print(ones_arr)\n",
        "print(\"\\nData type of the array:\",ones_arr.dtype)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EOunyMourikG",
        "outputId": "ffc81773-de77-4d2c-fdb3-55bdb77ccb73"
      },
      "id": "EOunyMourikG",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1. 1. 1. 1. 1. 1.]\n",
            "\n",
            "Data type of the array: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "x = np.arange(10)\n",
        "print(\"x=\",x)\n",
        "\n",
        "print(\"\\n x[:5] = \",x[:5])\n",
        "print(\"\\n x[5:] = \",x[5:])\n",
        "print(\"\\n x[4:7] = \",x[4:7])\n",
        "print(\"\\n x[::2] = \",x[::2])\n",
        "print(\"\\n x[1::2] = \",x[1::2])\n",
        "print(\"\\n x[::-1] = \",x[::-1])\n",
        "print(\"\\n x[5::-2] = \",x[5::-2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yK6mjXyMwNtw",
        "outputId": "81255fe3-8617-4063-e391-ab6aeac5416f"
      },
      "id": "yK6mjXyMwNtw",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x= [0 1 2 3 4 5 6 7 8 9]\n",
            "\n",
            " x[:5] =  [0 1 2 3 4]\n",
            "\n",
            " x[5:] =  [5 6 7 8 9]\n",
            "\n",
            " x[4:7] =  [4 5 6]\n",
            "\n",
            " x[::2] =  [0 2 4 6 8]\n",
            "\n",
            " x[1::2] =  [1 3 5 7 9]\n",
            "\n",
            " x[::-1] =  [9 8 7 6 5 4 3 2 1 0]\n",
            "\n",
            " x[5::-2] =  [5 3 1]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "x2 = np.array([[12, 5, 2, 4], [7, 6, 8, 8], [1, 6, 7, 7]])\n",
        "print(\"x2=\",x2)\n",
        "\n",
        "print(\"\\n x2[:2, :3] = \\n\",x2[:2, :3])\n",
        "print(\"\\n x2[2:, ::2]=\\n \",x2[2:, ::2])\n",
        "print(\"\\n x2[::-1, ::-1]= \\n\",x2[::-1, ::-1])\n",
        "print(\"\\n x2[::-1]= \\n\",x2[::-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oVCk4Wt3wwZf",
        "outputId": "be44deb8-67ea-4139-9865-bc4bcefebeca"
      },
      "id": "oVCk4Wt3wwZf",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x2= [[12  5  2  4]\n",
            " [ 7  6  8  8]\n",
            " [ 1  6  7  7]]\n",
            "\n",
            " x2[:2, :3] = \n",
            " [[12  5  2]\n",
            " [ 7  6  8]]\n",
            "\n",
            " x2[2:, ::2]=\n",
            "  [[1 7]]\n",
            "\n",
            " x2[::-1, ::-1]= \n",
            " [[ 7  7  6  1]\n",
            " [ 8  8  6  7]\n",
            " [ 4  2  5 12]]\n",
            "\n",
            " x2[::-1]= \n",
            " [[ 1  6  7  7]\n",
            " [ 7  6  8  8]\n",
            " [12  5  2  4]]\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
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
      "version": "3.9.12"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}