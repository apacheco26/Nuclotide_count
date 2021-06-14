import pandas as pd
import streamlit as st
import altair as alt


st.write("""
Julian's Project DNA Nucleotide Count Web App

This application counts the nucleotides composition of the provided DNA sequence

""")

st.header('Enter DNA sequence')

# Example DNA sequence to run the illustrate the program capabilities
DNA_sequence = ""

# runs the sequence DNA in a textbox joining the lines together in case of spaces
sequence = st.text_area("DNA input", DNA_sequence, height=250)
sequence = sequence.upper()
sequence =''.join(sequence)

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')

# counts the Adenine, thymine, guanine, and cytosine

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
        ])
    return d

count_DNA = DNA_nucleotide_count(sequence)

count_DNA

st.subheader('2. Display text')
st.write('There are  ' + str(count_DNA['A']) + ' adenine (A)')
st.write('There are  ' + str(count_DNA['T']) + ' thymine (T)')
st.write('There are  ' + str(count_DNA['G']) + ' guanine (G)')
st.write('There are  ' + str(count_DNA['C']) + ' cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(count_DNA, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)
