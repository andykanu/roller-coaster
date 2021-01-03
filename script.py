import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

mycmap = cm.get_cmap(name="Paired", lut=10)

# load rankings data here:
wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
# print(steel.head())
# print(wood.head())


# write function to plot rankings over time for 1 roller coaster here:
def show_ranking(roller_coaster, df, park_name):
    park_df = df[df["Park"] == park_name]
    year_of_rank = park_df["Year of Rank"].tolist()
    rank = park_df["Rank"].tolist()
    ax = plt.subplot()
    ax.set_ylabel("Rank")
    ax.set_xlabel("Year")
    ax.set_yticks(rank)
    ax.axes.invert_yaxis()
    plt.title("{0} in {1} ranking".format(roller_coaster, park_name))
    plt.plot(year_of_rank, rank)
    plt.show()


# write function to plot rankings over time for 2 roller coasters here:
def show_two_ranking(roller_coaster1, roller_coaster2, df, park_name1, park_name2):
    park1_df = df[df["Park"] == park_name1]
    park2_df = df[df["Park"] == park_name1]
    year_of_rank1 = park1_df["Year of Rank"].tolist()
    year_of_rank2 = park2_df["Year of Rank"].tolist()
    rank1 = park1_df["Rank"].tolist()
    rank2 = park2_df["Rank"].tolist()
    # plt.title("{0} in {1} ranking".format(roller_coaster, park_name))
    ax = plt.subplot(2, 1, 1)
    ax.set_ylabel("Rank")
    ax.set_xlabel("Year")
    ax.set_xticks(year_of_rank1)
    ax.set_yticks(rank1)
    ax.axes.invert_yaxis()
    ax.set_title(roller_coaster1)
    plt.plot(year_of_rank1, rank1)
    ax = plt.subplot(2, 1, 2)
    ax.set_ylabel("Rank")
    ax.set_xlabel("Year")
    ax.set_yticks(rank1)
    ax.set_xticks(year_of_rank2)
    ax.axes.invert_yaxis()
    ax.set_title(roller_coaster2)
    plt.plot(year_of_rank2, rank2)
    plt.subplots_adjust(hspace=1.0)
    plt.show()


# write function to plot top n rankings over time here:
def top_n_rankings(n, df):
    top_n_rankings = df[df["Rank"] <= n]
    ax = plt.subplot()
    for coaster in set(top_n_rankings["Name"]):
        coaster_rankings = top_n_rankings[top_n_rankings["Name"] == coaster]
        ax.plot(
            coaster_rankings["Year of Rank"], coaster_rankings["Rank"], label=coaster
        )
        ax.axes.invert_yaxis()
        ax.set_ylabel("Rank")
        ax.set_xlabel("Year")
        ax.set_yticks(top_n_rankings["Rank"])
        ax.set_xticks(top_n_rankings["Year of Rank"])
        ax.legend(
            bbox_to_anchor=(1, 0, 1, 0),
            loc="lower left",
            mode="expand",
            ncol=1,
        )
    plt.title("Top {0} roller coasters by year".format(n))
    plt.show()


# part 2 - roller coaster data

roller_data = pd.read_csv("roller_coasters.csv")
# print(roller_data.info())

# histogram of roller coaster data where numeric data passed in.
def create_histogram(df, col):
    if df[col].dtypes == "float64" or df[col].dtypes == "int64":
        if col == "num_inversions":
            col_name = "# inversions"
        else:
            col_name = col
        df.hist(column=col, bins=100, color="#ef9cbb")
        plt.ylabel("# roller coasters")
        plt.xlabel(col_name)
        plt.title("Roller Coasters by " + col_name)
        plt.show()
    else:
        print(
            "That column doesn't appear to contain a number. please check and try again"
        )


# create a bar chart showing number of inversions of rollercoasters per park
def create_bar_chart(df, park_name):
    plt.figsize = (10, 10)
    plotdata = df[df["park"] == park_name]
    print(plotdata["name"], plotdata["num_inversions"])
    plotdata.plot(
        kind="bar",
        x="name",
        y="num_inversions",
        color="#74cce1",
    )
    plt.xlabel("Roller Coasters")
    plt.ylabel("Number of Inversions")
    plt.title("Inversions by roller coaster in " + park_name)
    plt.show()


# pie chart showing how many coasters in operation vs how many closed
def operating_status_pie(df):
    livestatus = df[df["status"] == "status.operating"].name.nunique()
    deadstatus = df[df["status"] == "status.closed.definitely"].name.nunique()
    plt.pie(
        [livestatus, deadstatus],
        labels=["Operating", "Closed"],
        explode=(0.1, 0),
        colors=["#1ab1cd", "#32d9cb"],
        shadow=True,
        autopct="%1.0f%%",
        pctdistance=1.3,
    )
    plt.title("Operating vs. Closed roller coasters")
    plt.axis("equal")
    plt.legend(frameon=False, bbox_to_anchor=(1.5, 0.8))
    plt.show()


# scatter plot for two numeric variables in rollercoaster data
def scatter(df, col1, col2):
    plt.figsize = (15, 10)
    plt.scatter(df[col1], df[col2], c="darkblue", alpha=0.15)
    plt.title("{0} vs {1}".format(col1, col2))
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()


print(roller_data.head())
print(roller_data.info())

# What seating type is most popular?
def seating_type(df):
    seat_count = (
        df.groupby("seating_type")
        .name.count()
        .sort_values(ascending=False)
        .reset_index()
    )
    plt.figsize = (15, 10)
    plt.pie(
        seat_count["name"],
        autopct=lambda p: str(p.round(1)) + "%" if p >= 1 else None,
        pctdistance=1.3,
    )
    plt.axis("equal")
    plt.title("Roller Coaster by seating type")
    plt.legend(
        labels=seat_count["seating_type"], loc="center left", bbox_to_anchor=(1.0, 0.5)
    )
    plt.show()


# next challenge is to return seating type by [numeric] - could use FacetGrid???
seating_type(roller_data)