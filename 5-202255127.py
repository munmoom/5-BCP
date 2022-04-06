{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "5-202255127.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP3qnGfqI6qlsJeGxp0yNl1",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/5-BCP/blob/main/5-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import collections\n",
        "\n",
        "A = str(input())\n",
        "A = A.lower()\n",
        "A = collections.Counter(A)\n",
        "\n",
        "\n",
        "num = A.values()\n",
        "num = list(num)\n",
        "\n",
        "\n",
        "num.sort()\n",
        "big = num[0]\n",
        "big = int(big)\n",
        "\n",
        "reverse_A = dict(map(reversed,A.items()))\n",
        "print(reverse_A)\n",
        "reverse_A.get(big).upper()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 72
        },
        "id": "SXs_MWbwqalY",
        "outputId": "bc74f448-a1c1-4e41-b3cf-61132a007c0d"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "YYYYDJJJJ\n",
            "{4: 'j', 1: 'd'}\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'D'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    }
  ]
}