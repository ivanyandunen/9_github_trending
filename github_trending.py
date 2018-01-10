import requests
import datetime


def get_trending_repositories(top_size):
    week = 7
    url = 'https://api.github.com/search/repositories'
    search_date = datetime.date.today() - datetime.timedelta(week)
    params = {
        'q': 'created:>={}'.format(search_date),
        'sort': 'stargazers_count',
        'order': 'desc',
        'per_page': 'top_size'
    }

    response = requests.get(url, params).json()

    return response['items']


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )

    return len(requests.get(url).json())


if __name__ == '__main__':
    top_size = 20
    repositories = get_trending_repositories(top_size)
    for repo in repositories:
        repo_owner = repo['owner']['login']
        repo_name = repo['name']
        repo_url = repo['url']
        print('Repository name: {}'.format(repo_name))
        print('Url: {}'.format(repo_url))
        print(
            'Open issues: {}'
            .format(get_open_issues_amount(repo_owner, repo_name)),
            end='\n\n'
        )
