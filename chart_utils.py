def format_chart_data(rows):
    labels = []
    values = []

    for row in rows:
        labels.append(row[0])
        values.append(float(row[1]) if row[1] else 0)

    return {
        "labels": labels,
        "values": values
    }


def prepare_revenue_chart(monthly_revenue):
    months = []
    revenues = []

    for revenue in monthly_revenue:
        months.append(revenue[0])
        revenues.append(float(revenue[1]))

    return months, revenues


def prepare_status_count_chart(data):
    labels = []
    counts = []

    for item in data:
        labels.append(item[0])
        counts.append(item[1])

    return labels, counts