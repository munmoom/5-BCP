{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "3-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyOxj8u1q88OvTGHh2r2VAex",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/5-BCP/blob/main/3_202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "(1) "
      ],
      "metadata": {
        "id": "2R9Ep9jE0JbE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "metro = ['서울','부산','인천','대구','광주','대전','울산']\n",
        "metro.append('제주')\n",
        "print(metro)\n",
        "metro.sort()\n",
        "print(metro)\n",
        "metro.reverse()\n",
        "print(metro)\n",
        "print(metro.index('부산'))\n",
        "metro.insert(3,'강원')\n",
        "print(metro)\n",
        "metro.remove('대구')\n",
        "print(metro)\n",
        "metro.pop()\n",
        "print(metro)\n",
        "print(metro.count('인천'))\n",
        "metro.extend(['대구','광주'])\n",
        "print(metro)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rJb_nYlBDjL6",
        "outputId": "2b09b846-d4ed-4fc8-f59e-1fc5cc41c03a"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['서울', '부산', '인천', '대구', '광주', '대전', '울산', '제주']\n",
            "['광주', '대구', '대전', '부산', '서울', '울산', '인천', '제주']\n",
            "['제주', '인천', '울산', '서울', '부산', '대전', '대구', '광주']\n",
            "4\n",
            "['제주', '인천', '울산', '강원', '서울', '부산', '대전', '대구', '광주']\n",
            "['제주', '인천', '울산', '강원', '서울', '부산', '대전', '광주']\n",
            "['제주', '인천', '울산', '강원', '서울', '부산', '대전']\n",
            "1\n",
            "['제주', '인천', '울산', '강원', '서울', '부산', '대전', '대구', '광주']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "(2) "
      ],
      "metadata": {
        "id": "dN3G9VUU0c06"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "WVf6cQiu0A88",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "623b0b4d-b030-422d-aebe-46e2e500795f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'02': '서울', '051': '부산', '031': '인천', '053': '대구', '062': '광주', '042': '대전', '052': '울산'}\n",
            "{'02': '서울', '051': '부산', '031': '인천', '053': '대구', '062': '광주', '042': '대전', '052': '울산'}\n",
            "{'02': '서울', '051': '부산', '031': '인천', '053': '대구', '062': '광주', '042': '대전', '052': '울산'}\n",
            "{}\n",
            "{'02': '서울', '051': '부산', '031': '인천', '053': '대구', '062': '광주', '042': '대전', '052': '울산', '064': '제주'}\n",
            "031\n",
            "{}\n",
            "{'051': '부산'}\n"
          ]
        }
      ],
      "source": [
        "met_num = {'02':'서울', '051':'부산', '031':'인천', '053':'대구', '062':'광주', '042':'대전', '052':'울산'}\n",
        "met_num2 = {'02':'서울', '051':'부산', '031':'인천', '053':'대구', '062':'광주', '042':'대전', '052':'울산', '064':'제주'}\n",
        "met_num.keys()\n",
        "print(met_num)\n",
        "met_num.values()\n",
        "print(met_num)\n",
        "met_num.items()\n",
        "print(met_num)\n",
        "met_num.clear()\n",
        "print(met_num)\n",
        "met_num.update(met_num2)\n",
        "met_num.get('064')\n",
        "print(met_num)\n",
        "\n",
        "b = {'051':'부산'}\n",
        "i = str(input())\n",
        "\n",
        "if i in met_num:\n",
        "  met_num.clear()\n",
        "  print(met_num)\n",
        "  met_num.update(b)\n",
        "  print(met_num)\n",
        "else:\n",
        "  del met_num"
      ]
    }
  ]
}