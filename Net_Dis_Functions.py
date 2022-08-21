import plotly.express as px
from plotly.offline import plot
import dill as pickle

def payload(data, geo, time, pytrends):
    if geo == 'Default':
        pytrends.build_payload(kw_list = data, timeframe=time)
    else:
        pytrends.build_payload(kw_list = data, geo = geo , timeframe=time)
    df = pytrends.interest_over_time()
    df = df.drop(['isPartial'], axis=1)
    return df, pytrends

def LinePlot(df, col, title, xTitle, yTitle,plot_file):
    fig = px.line(df, x=df.index, y=col)
    # Edit the layout
    fig.update_layout(title=title,
                   xaxis_title=xTitle,
                   yaxis_title=yTitle)
    fig.show()
    plot(fig, filename = plot_file+'.html')
    with open(plot_file+'.pkl', 'wb') as pickle_file:
        pickle.dump(fig, pickle_file,  pickle.HIGHEST_PROTOCOL)