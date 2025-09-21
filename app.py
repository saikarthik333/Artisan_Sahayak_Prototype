import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Artisan-Sahayak Prototype",
    page_icon="🤝",
    layout="centered"
)

# --- Session State Initialization ---
if 'stage' not in st.session_state:
    st.session_state.stage = 'start_screen'

# --- Helper Functions ---
def set_stage(stage):
    st.session_state.stage = stage

# --- Main App ---
st.title("Artisan-Sahayak Prototype 🤝")

# =============================================================================
# --- START SCREEN / SOCIAL MEDIA MOCKUP ---
# =============================================================================
if st.session_state.stage == 'start_screen':
    st.image(
        "assets/social_post.png",
        caption="This is how a customer discovers the artisan's work."
    )
    st.markdown("---")
    st.info("The customer sees the post and decides to message the artisan.")
    if st.button("Click here to Start the Chat Simulation", type="primary"):
        set_stage('chat_begin')

# =============================================================================
# --- CHAT SIMULATION ---
# =============================================================================
elif st.session_state.stage != 'start_screen':
    st.markdown("### AI-Powered Chat Simulation")

    # --- NEW: ADDED PRODUCT IMAGE HERE ---
    st.image(
        "assets/product_vase.png", # <-- Make sure you have this image
        caption="The 'Blue Terracotta Vase' by artisan Devi Lal."
    )
    # --- END OF NEW CODE ---

    view = st.radio(
        "Select Your View:",
        ('Customer View', 'Artisan View'),
        horizontal=True,
        label_visibility="collapsed"
    )
    st.markdown("---")

    # --- CUSTOMER VIEW LOGIC ---
    if view == 'Customer View':
        chat_container = st.container(height=400)
        with chat_container:
            if st.session_state.stage >= 'chat_begin':
                st.chat_message("user", avatar="🧑‍💻").write("Hi, I saw this on WhatsApp Status. Is this vase available?")
            if st.session_state.stage >= 'stage_1':
                st.chat_message("assistant", avatar="🤖").write("Hello! I am the AI Sahayak for Devi Lal... The price is **₹1,200 + shipping**.")
            if st.session_state.stage >= 'stage_3':
                 st.chat_message("user", avatar="🧑‍💻").write("I would like to buy it. I live in Bangalore.")
            if st.session_state.stage >= 'stage_4':
                st.chat_message("assistant", avatar="🤖").write("Wonderful! ...please provide your full delivery address.")
            if st.session_state.stage >= 'stage_5':
                st.chat_message("user", avatar="🧑‍💻").write("Priya Sharma, 123, Blossom Gardens, Indiranagar, Bangalore, 560038.")
            if st.session_state.stage >= 'stage_6':
                st.chat_message("assistant", avatar="🤖").write("Thank you, Priya. Your order total is ₹1,200 (Vase) + ₹90 (Shipping) = **₹1,290**.")
            if st.session_state.stage >= 'stage_7':
                st.chat_message("assistant", avatar="🤖").write("Payment successful! Thank you... We have notified Devi Lal...")
            if st.session_state.stage >= 'stage_8':
                 with st.chat_message("assistant", avatar="🤖"):
                    st.write("As a special token of appreciation, here is the Certificate of Authenticity...")
                    st.image("assets/certificate.png", caption="Pramanik-Patra (Certificate of Authenticity)")

        # --- User Input Logic ---
        if st.session_state.stage == 'chat_begin':
            st.button("Send Message", on_click=set_stage, args=['stage_1'])
        if st.session_state.stage == 'stage_1':
            if st.text_input("Your reply...", key="reply1", placeholder="Type your reply..."):
                set_stage('stage_3')
        if st.session_state.stage == 'stage_3':
            st.button("Send Reply", on_click=set_stage, args=['stage_4'])
        if st.session_state.stage == 'stage_4':
            if st.text_input("Your address...", key="address1", placeholder="Type your address..."):
                set_stage('stage_6')
        if st.session_state.stage == 'stage_6':
            st.button("Pay ₹1,290 via UPI", on_click=set_stage, args=['stage_7'])
        if st.session_state.stage == 'stage_7':
            time.sleep(1) 
            set_stage('stage_8')
        if st.session_state.stage >= 'stage_8':
            st.success("End of Customer Demo.")
            if st.button("Reset Demo"):
                set_stage('start_screen')

    # --- ARTISAN VIEW LOGIC ---
    elif view == 'Artisan View':
        st.info("This is the artisan's private chat with their AI Sahayak.", icon="🧑‍🎨")
        chat_container = st.container(height=300)
        with chat_container:
            if st.session_state.stage >= 'stage_1':
                with st.chat_message("assistant", avatar="🤖"):
                    st.write("Namaste Devi Lal ji 🙏")
                    st.info("New order inquiry... No action needed from you yet.", icon="💬")
            if st.session_state.stage >= 'stage_7':
                with st.chat_message("assistant", avatar="🤖"):
                    st.success("Payment of **₹1,290** has been received...", icon="✅")
                    st.warning("**ACTION NEEDED:** Please pack the item... send me a photo of the box.", icon="📦")
        if st.session_state.stage < 'stage_1':
            st.write("No new updates yet.")