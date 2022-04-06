{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "4-202255127.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNbaFwcxdgzbeFOi6F1uKFu",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/5-BCP/blob/main/4-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trash = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']\n",
        "\n",
        "words = input()\n",
        "words = words.split()\n",
        "words = list(words)\n",
        "\n",
        "abb = words[0][0].upper()\n",
        "words = words[1:]\n",
        "\n",
        "for word in words:\n",
        "  if word not in trash:\n",
        "    abb = abb + word[0].upper()\n",
        "\n",
        "print(abb)"
      ],
      "metadata": {
        "id": "WetiJ5GQxKBa",
        "outputId": "faa6f21f-ec61-4ec4-eac8-8dedb3774da2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i pa spagette like milk\n",
            "ISLM\n"
          ]
        }
      ]
    }
  ]
}