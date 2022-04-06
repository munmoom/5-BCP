{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNjpGcVsDzG8kcXeEIfQqf6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/munmoom/5-BCP/blob/main/2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for a in range(1, 30):\n",
        " for b in range(a, 30):\n",
        "  for c in range(b, 30):\n",
        "   if c**2 == a**2 + b**2:\n",
        "     pita_list.append([a,b,c]) \n",
        "\n",
        "pita_list"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vVupRGxDle3e",
        "outputId": "4a19143d-773b-4028-efcf-e3a80129232f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[3, 4, 5],\n",
              " [5, 12, 13],\n",
              " [6, 8, 10],\n",
              " [7, 24, 25],\n",
              " [8, 15, 17],\n",
              " [9, 12, 15],\n",
              " [10, 24, 26],\n",
              " [12, 16, 20],\n",
              " [15, 20, 25],\n",
              " [20, 21, 29]]"
            ]
          },
          "metadata": {},
          "execution_count": 47
        }
      ]
    }
  ]
}