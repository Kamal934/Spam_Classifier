import streamlit as st
st.set_page_config(page_title='Dashboard_page', page_icon=':world_map:')

def main():
    with open("style.css", "r") as css_file:
        custom_css = f"<style>{css_file.read()}</style>"
        st.markdown(custom_css, unsafe_allow_html=True)
    st.title(":email: Email ")
    custom_css = """
    <style>
    css-1y4p8pa {
    width: 100%;
    padding: 6rem 1rem 10rem;
    max-width:1400rem
    }
    
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    chart_html = """
    <div class= container>
    <canvas id="myChart"></canvas>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['ham','spam'],
            datasets: [{
                label: 'Spam volums',
                data: [67,33],
                backgroundColor: [
                    'rgb(101, 39, 190,0.5)',
                    'rgb(10, 207, 221,0.5)'
                ],
                borderColor: [
                    'rgb(101, 39, 190,1)',
                    'rgb(10, 207, 221,1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
        }
    });
    </script>
    """
    accuracy_chart = """
    <canvas id="myChart" width="400" height="400"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Bnb','Gnb','Mnb','A_bost','G_bost','R_bost'],
            datasets: [
            {
            label: "accuracy",
            data: [93.3,97.5,94.1,97.4,97.8,98.3],
            'backgroundColor': [
            'rgb(233, 102, 160,0.5)',
            'rgb(43, 39, 48,0.5)',
            'rgba(25, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgb(101, 84, 175,0.5)'
        ],
        'borderColor': [
            'rgb(233, 102, 160,1)',
            'rgb(43, 39, 48,1)',
            'rgba(55, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgb(101, 84, 175,1)'
        ],
        'borderWidth': 2
        }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
    </script>
    """
    Metrics_chart = """
    <canvas id="myChart" width="400" height="400"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Bnb','Gnb','Mnb','A_bost','G_bost','R_bost'],
            datasets: [
            {
            label: "Precision",
            data: [95.3,97,98.5,94.7,98.6,99.9],
            backgroundColor: "rgb(233, 102, 160,1)"
          },
          {
            label: "Recall",
            data: [83.1,84.8,82.88,97.3,94.6,95.7],
            backgroundColor: "rgb(43, 39, 48,1)"
          },
          {
            label: "F1-score",
            data: [88.8,90.8,90.0,96.0,96.5,97.2],
            backgroundColor: "rgb(101, 84, 175,1)"
          }

        ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
    </script>
    """
    TRAIN_chart = """
    <canvas id="pie_Chart" width="400" height="410"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
var ctx = document.getElementById("pie_Chart").getContext("2d");
    var myChart = new Chart(ctx, {
    type: "pie",
    data: {
        labels: ["Log-Regr", "Rand-Forest", "Deci- Tree", "SVM"],
        datasets: [{
            label: "Spam Volume",
            data: [10, 20, 30, 40],
        'backgroundColor': [
            'rgb(255, 184, 76,0.5)',
            'rgb(101, 84, 175,0.5)',
            'rgba(25, 206, 86, 0.5)',
            'rgb(152, 33, 118,0.5)',
            'rgba(155, 159, 64, 0.5)'
        ],
        'borderColor': [
            'rgb(255, 184, 76,1)',
            'rgb(101, 84, 175,1)',
            'rgba(55, 206, 86, 1)',
            'rgb(152, 33, 118,1)',
            'rgba(255, 159, 64, 1)'
        ],
        'borderWidth': 1
        }]
    },
    options: {
        title: {
        text: "My First Chart"
        },
        legend: {
        position: "bottom",
        
        labels: {
            fontColor: "white",
            fontFamily: "sans-serif",
            fontSize: 15,
            fontStyle: "italic",
            backgroundColor: "#00000",
            borderColor: "#FFFFFF"
        }
        }
    }
    });
    </script>
    """
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.subheader(":bar_chart: Quality Datasets")
        st.markdown(" % in data" )
        st.components.v1.html(chart_html, height=250,width=250)
    with col2:
        st.subheader(":earth_asia: Accuracy")
        st.markdown(" % in data" )
        st.components.v1.html(accuracy_chart, height=250,width=250)
    with col3:
        st.subheader(":dart: Metrics(P,R,F1)")
        st.markdown(" % in data" )
        st.components.v1.html(Metrics_chart, height=250,width=250)
    with col4:
        st.subheader(":brain: Train")
        st.markdown(" % in data" )
        st.components.v1.html(TRAIN_chart, height=250,width=250)
if __name__ == "__main__":
    main()
def main():
    st.title(":ice_cube: SMS ")

    chart_html = """
    <canvas id="myChart" width="400" height="400"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['ham','spam'],
            datasets: [{
                label: 'Spam volums',
                data: [57,43],
                backgroundColor: [
                    'rgba(0,0,125, 0.5)',
                    'rgba(128,0,0, 0.5)'
                ],
                borderColor: [
                    'rgba(0,0,125, 1)',
                    'rgba(128,0,0, 1)'
                ],
                borderWidth: 1
            }]
        },
    });
    </script>
    """
    accuracy_chart = """
    <canvas id="myChart" width="400" height="400"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Bnb','Gnb','Mnb','A_bost','G_bost','R_bost'],
            datasets: [
            {
            label: "accuracy",
            data: [87.8,97.5,98.0,97.5,97.3,97.4],
            'backgroundColor': [
            'rgba(199,21,133, 0.8)',
            'rgba(54, 162, 235, 0.7)',
            'rgba(125, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.9)',
            'rgba(155, 159, 64, 0.5)'
        ],
        'borderColor': [
            'rgba(199,21,133, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(125, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(155, 159, 64, 1)'
        ],
        'borderWidth': 1
        }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
    </script>
    """
    Metrics_chart = """
    <canvas id="myChart" width="400" height="400"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Bnb','Gnb','Mnb','A_bost','G_bost','R_bost'],
            datasets: [
            {
            label: "Precision",
            data: [54,97,94,98,99,100],
            backgroundColor: "rgb(95, 33, 72,1)"
            },
          {
            label: "Recall",
            data: [84.0,84.8,91.7,84.2,81.3,83.3],
            backgroundColor: "rgb(136, 14, 178,1)"
          },
          {
            label: "F1-score",
            data: [66.2,90.8,93.0,90.8,89.3,90.9],
            backgroundColor: "rgb(162, 89, 4,1)"
          }

        ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
    </script>
    """
    TRAIN_chart = """
    <canvas id="pie_Chart" width="400" height="410"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
var ctx = document.getElementById("pie_Chart").getContext("2d");
    var myChart = new Chart(ctx, {
    type: "pie",
    data: {
        labels: ["Log-Regr", "Rand-Forest", "Deci-Tree", "SVM"],
        datasets: [{
            label: "Spam Volume",
            data: [10, 20, 30, 40],
        'backgroundColor': [
            'rgb(250, 142, 18,0.5)',
            'rgb(61, 207, 149,0.5)',
            'rgb(45, 3, 214,0.5)',
            'rgb(23, 92, 65,0.5)'
        ],
        'borderColor': [
            'rgb(250, 142, 18,1)',
            'rgb(61, 207, 149,1)',
            'rgb(45, 3, 214,1)',
            'rgb(23, 92, 65,1)'
        ],
        'borderWidth': 1
        }]
    },
    options: {
        title: {
        text: "My First Chart"
        },
        legend: {
        position: "bottom",
        
        labels: {
            fontColor: "white",
            fontFamily: "sans-serif",
            fontSize: 15,
            fontStyle: "italic",
            backgroundColor: "#00000",
            borderColor: "#FFFFFF"
        }
        }
    }
    });
    </script>
    """
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.subheader(":bar_chart: Quality Datasets")
        st.markdown(" % in data" )
        st.components.v1.html(chart_html, height=250,width=250)
    with col2:
        st.subheader(":earth_asia: Accuracy")
        st.markdown(" % in data" )
        st.components.v1.html(accuracy_chart, height=250,width=250)
    with col3:
        st.subheader(":dart: Metrics(P,R,F1)")
        st.markdown(" % in data" )
        st.components.v1.html(Metrics_chart, height=250,width=250)
    with col4:
        st.subheader(":brain: Train")
        st.markdown(" % in data" )
        st.components.v1.html(TRAIN_chart, height=250,width=250)
if __name__ == "__main__":
    main()


    # st.header(" World Overview ")
    # st.subheader("% in data")
custom_css = """
<style>
.reportview-container .main .block-container {
    
    # padding: 0%;
    .stApp {
    margin: 0;
}
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
world_overview = """
<canvas id="myChart" width="400" height="400"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [ "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"
        ,"2020", "2021", "2022"],
    
        datasets: [{
        label: "India",
        data: [3.2,3.8,4.4,5.0,5.6,6.2,6.8,7.4,7.8,8.2,8.6],
        borderColor: "rgb(6,18,208,1)"


        },
        {
        label: "China",
        data: [5.2,6.6,8.0,9.4,10.8,12.2,13.6,15.0,16.4,17.8,19.2],
        borderColor: "rgb(101, 40, 247,1)",
        }, {
        label: "Brazil",
        data: [2.8,3.4,4.0,4.6,5.2,5.8,6.4,7.0,7.6,8.2,8.8],
        borderColor: "rgb(245, 53, 87,1)",
        }, {
        label: "US",
        data: [7.2,8.6,10.0,11.4,12.8,14.2,15.6,17.0,18.4,19.8,21.2],
        borderColor: "rgb(14, 128, 32,1)",
        }, {
        label: "Iceland",
        data: [0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14],
        borderColor: "rgb(3, 102, 31,1)",
        }

    ]
        
    },
    options: {
    }
});
</script>
"""
india="""
<canvas  id="barLine" height="150",width="300"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
var ctx = document.getElementById("barLine").getContext("2d");
    var myChart = new Chart(ctx, {
    type: "pie",
    data: {
        labels: ["jun","May","April","Mar","Feb"],
        datasets: [{
        label: "Spam Volume",
        data: [23.4, 22.1, 21.2,20.3,19.4],
        'backgroundColor': [
            'rgb(137, 29, 133,0.5)',
            'rgb(101, 40, 247,0.5)',
            'rgb(80, 93, 47,0.5)',
            'rgb(95, 99, 117,0.5)',
            'rgb(79, 84, 163,0.5)'
        ],
        'borderColor': [
            'rgb(137, 29, 133,1)',
            'rgb(101, 40, 247,1)',
            'rgb(80, 93, 47,1)',
            'rgb(95, 99, 117,1)',
            'rgb(79, 84, 163,1)'
        ],
        'borderWidth': 1
        }]
    },
    options: {
        title: {
        text: "My First Chart"
        },
        legend: {
        position: "bottom",
        
        labels: {
            fontColor: "white",
            fontFamily: "sans-serif",
            fontSize: 15,
            fontStyle: "italic",
            backgroundColor: "#00000",
            borderColor: "#FFFFFF"
        }
        }
    }
    });
    </script>
"""
left_column, right_column= st.columns([1,1])

with st.container():

    with left_column:
        st.subheader(":world_map: World Overview")
        st.markdown(" % in data" )
        st.components.v1.html(world_overview, height=350,width=359)
    with right_column:
        st.subheader(":place_of_worship: India all Spam data (in millions) in 2023")
        st.markdown("data in billions" )
        st.components.v1.html(india, height=350,width=350)
        st.markdown("In 2023, India had the highest spam volume of the three countries,")
        st.markdown(" with 11.4 billion spam messages.")


def main():
    india_chart="""
    <canvas  id="barLine" height="150",width="300"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
var ctx = document.getElementById("barLine").getContext("2d");
    var myChart = new Chart(ctx, {
    type: "pie",
    data: {
        labels: ["Gmail","Yahoo","SMS","Whsapp","Insta","Facebook"],
        datasets: [{
        label: "Spam Volume",
        data: [3.2, 1.6, 6.2,2.4,1.8,1.2],
        'backgroundColor': [
            'rgb(0, 63, 92, 0.5)',
            'rgb(88, 80, 141, 0.5)',
            'rgb(202, 10, 44,0.5)',
            'rgb(188, 80, 144, 0.5)',
            'rgb(107, 141, 1, 0.5)',
            'rgb(161, 64, 0, 0.5)'
        ],
        'borderColor': [
            'rgba(0, 63, 92, 1)',
            'rgba(88, 80, 141, 1)',
            'rgb(202, 10, 44,1)',
            'rgb(188, 80, 144, 1)',
            'rgb(107, 141, 1, 1)',
            'rgb(161, 64, 0, 1)'
        ],
        'borderWidth': 2
        }]
    },
    options: {
        title: {
        text: "My First Chart"
        },
        legend: {
        position: "bottom",
        
        labels: {
            fontColor: "white",
            fontFamily: "sans-serif",
            fontSize: 15,
            fontStyle: "italic",
            backgroundColor: "#00000",
            borderColor: "#FFFFFF"
        }
        }
    }
    });
    </script>"""

    india_Chart2=""" <canvas  id="barLine1" height="150",width="300"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
    var ctx = document.getElementById("barLine1").getContext("2d");
        var myChart = new Chart(ctx, {
        type: "pie",
        data: {
            labels: ["MH","UP","Karnataka","TN","Delhi"],
            datasets: [{
            label: "Spam Volume",
            data: [42.5, 37.2, 28.4,25.6,24.2],
            'backgroundColor': [
                'rgb(32, 133, 23, 0.5)',
                'rgb(132, 100, 160, 0.5)',
                'rgb(150, 50, 50, 0.5)',
                'rgb(101, 40, 247,0.5)',
                'rgb(233, 102, 160,0.5)'
            ],
            'borderColor': [
                'rgb(32, 133, 23, 1)',
                'rgb(132, 100, 160, 1)',
                'rgb(150, 50, 50, 1)',
                'rgb(101, 40, 247,1)',
                'rgb(233, 102, 160,1)'
            ],
            'borderWidth': 2
            }]
        },
        options: {
            legend: {
            position: "bottom",
            
            labels: {
                fontColor: "white",
                fontFamily: "sans-serif",
                fontSize: 15,
                fontStyle: "italic",
                backgroundColor: "#00000",
                borderColor: "#FFFFFF"
            }
            }
        }
        });
        </script>
    """
    col1,col2=st.columns(2)
    with st.container():
        with col1:
            st.subheader(":placard: India  Spam Sms data in 2023")
            st.markdown("data in millions")
            st.components.v1.html(india_chart, height=350,width=350)
            st.markdown("In 2023,Spam emails are a serious problem in India,")
            st.markdown(" especially in the top 5 states.")
        with col2:
            st.subheader("	:hourglass_flowing_sand: Top 5 Platforms for Spam in India 2023")
            st.markdown("data in Billions")
            st.components.v1.html(india_Chart2, height=350,width=350)
            st.markdown("The spam data detected by the CoE Spam Committee is likely to be")
            st.markdown("an underestimation of the actual amount of spam data sent in India in 2023.")
if __name__ == "__main__":
    main()
# news




# markdown removwe
hide_st_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>"""
st.markdown(hide_st_style,unsafe_allow_html=True)