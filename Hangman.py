import random
import streamlit as st
# import base64
def init():
    if 'com' not in st.session_state:
        words=['python','computer','technology','science','javascript','introduction']
        st.session_state.com=random.choice(words)
        st.session_state.attempts=6
        st.session_state.guesses=['_']*len(st.session_state.com)
        st.session_state.guessed=set()
        st.session_state.gameover=False
    
def image(imag):
        # with open(imag,'rb')as image:
        #     encode=base64.b64encode(image.read()).decode()
        st.markdown(
        f'''<style>
    .stApp{{

        background-image: url("{imag}");
        background-size: cover;
        background-position: top;
        background-repeat: no-repeat;
    }}
</style>''',unsafe_allow_html=True
    )
def game():
    image('https://github.com/Ghazanfar-G/Hangman-game/blob/main/ahangman.png?raw=true')

    st.title('🦸Welcome to Hangman game')
    init()

    st.write('You have to find a word by writting letters of word one by one. All the best.')
    st.write(f'Attempts : {st.session_state.attempts}')
    st.write('Word '+''.join(st.session_state.guesses))
    user=st.text_input('Enter letter here: ',key='user',value='').strip().lower()
    if st.button('Next'):
        if not user:
            st.warning('First enter a letter.')
            return
        if user in st.session_state.guessed:
            st.warning('You have already choose this letter.')
            return
        st.session_state.guessed.add(user)
        if user in st.session_state.com:
            for indexs,character in enumerate(st.session_state.com):
                if character == user:
                    st.session_state.guesses[indexs]=user
            if st.button('Continue'):
                st.rerun()
            st.success('✅Good guess')
        else:
            st.error('❌Wrong guess')
            st.session_state.attempts-=1


    if ''.join(st.session_state.guesses) == st.session_state.com:
        st.balloons()
        st.success('😉Congratulation, You are the winner.')
        st.success(f'The answer is {st.session_state.com}')
        st.session_state.gameover=True        
    elif st.session_state.attempts==0:
        st.snow()
        st.error(f'The answer is {st.session_state.com}')
        st.error('😞You lose. Please try again.')        
        st.session_state.gameover=True    
    if st.session_state.gameover:    
        if st.button('Play again'):
            st.session_state.clear()
            st.rerun() 
if __name__=='__main__':
    game()


