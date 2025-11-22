import streamlit as st

class MultiPage:
    """
    Class to manage multiple Streamlit pages
    """
    
    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name
        
        st.set_page_config(
            page_title=self.app_name,
            page_icon="📈",
            layout="wide"
        )
    
    def add_page(self, title, func):
        """
        Add a page to the app
        """
        self.pages.append({
            "title": title,
            "function": func
        })
    
    def run(self):
        """
        Run the app
        """
        # Header
        st.title(self.app_name)
        
        # Sidebar navigation
        st.sidebar.title("🧭 Navigation")
        page_titles = [page["title"] for page in self.pages]
        page = st.sidebar.radio("Go to:", page_titles)
        
        # Warning banner
        st.sidebar.markdown("---")
        st.sidebar.error("""
        ⚠️ **EDUCATIONAL ONLY**
        
        Models have weak predictive power (51% accuracy, R²=-0.037).
        
        **NOT for actual trading!**
        """)
        
        # Footer
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        📚 **TradeCare Project**
        
        Code Institute PP5
        Predictive Analytics
        
        [GitHub Dataset](https://github.com/mouadja02/bitcoin-hourly-ohclv-dataset)
        """)
        
        # Run selected page
        for page_dict in self.pages:
            if page_dict["title"] == page:
                page_dict["function"]()
                break