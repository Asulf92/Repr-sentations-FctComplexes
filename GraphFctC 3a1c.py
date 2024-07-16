import numpy as np
import plotly.graph_objects as go

density=range(-300,300,1)

def f(x): #f(x)=x²
    a=x[0]
    b=x[1]
    # a1=-a*b
    # b1=b+a
    a1=np.log(np.sin(a**2-b**2))
    b1=np.exp(np.log2(2*a*b))
    x=(a1,b1)
    return x


C=[[],[],[],[]]

for a in density:
    for b in density:
        r=(a,b)
        t=f(r)
        C[0].append(a)
        C[1].append(b)
        C[2].append(t[0])
        C[3].append(t[1]+3)

# print(C[0])
# print(C[1])
# print(C[2])
# print(C[3])

x = np.array(C[0])
y = np.array(C[1])
z = np.array(C[2])
colors = np.array(C[3])

fig = go.Figure()


def plan():
    fig.add_trace(go.Scatter3d(
        x=[min(C[0]), max(C[0])], y=[0, 0], z=[0, 0], 
        mode='lines', 
        line=dict(
            color='blue',
            width=7)
        ))
    fig.add_trace(go.Scatter3d(
        x=[0, 0], y=[min(C[1]), max(C[1])], z=[0, 0], 
        mode='lines', 
        text="y",
        line=dict(
            color='yellow', 
            width=7)
        ))
    fig.add_trace(go.Scatter3d(
    x=[0, 0], y=[0, 0], z=[min(C[2]), max(C[2])], 
    mode='lines', 
    line=dict(
        color='purple', 
        width=7,)
    ))
plan()


fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z, 
    marker=dict(
        size=5,
        cmax=max(C[3]),
        cmin=min(C[3]),
        color=colors,
        opacity=0.1,
        colorbar=dict(
            title="Colorbar"
        ),
        colorscale=([0, 'rgb(0, 200, 0)'],[0.5, 'rgb(0, 0, 0)'], [1.0, 'rgb(200, 0, 0)'])
    ),
    mode="markers"))

# Forcer axes
# fig.update_layout(scene=dict(
#     xaxis=dict(range=[-5, 5], zeroline=False),
#     yaxis=dict(range=[-5, 5], zeroline=False),
#     zaxis=dict(range=[-5, 5], zeroline=False),
# ))

# Show the figure
fig.show()
