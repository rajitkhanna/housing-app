import streamlit as st
import streamlit.components.v1 as components

st.title('Hello World')
components.html(
"""
<script>
    (function(d, h, m){
        var js, fjs = d.getElementsByTagName(h)[0];
        if (d.getElementById(m)){return;}
        js = d.createElement(h); js.id = m;
        js.onload = function(){
            window.makerWidgetComInit({
            position: "right",          
            widget: "mrddprfg2xsqfftf-syo08gd3ig3kfcpu-derpk2u1gemdce4u"                
        })};
        js.src = "https://makerwidget.com/js/embed.js";
        fjs.parentNode.insertBefore(js, fjs)
    }(document, "script", "dhm"))
</script>
"""
)