# @time     ：2024/7/22 14:49
# @author   : 莉光哈哈哈
# @file     : test56_recommender_system.py
# @software : PyCharm
'''
1、准备数据-----构造一个评分矩阵
'''
import numpy as np

# 示例评分矩阵（用户×电影）
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5]
    [0, 0, 0, 4],
])

# 用户ID到行索引的映射
user_to_idx = {'Alice': 0, 'Bob': 1, 'Charlie': 2, 'David': 3}

# 电影ID到列索引的映射
movie_to_idx = {'Movie A': 0, 'Movie B': 1, 'Movie C': 2, 'Movie D': 3}

'''
2.计算用户间的相似度----使用余弦相似度来衡量用户之间的相似性
'''


def cosine_similarity(user_ratings):
    '''
    计算用户评分向量的余弦相似度
    :param user_ratings:
    :return:
    '''
    norm = np.sqrt((user_ratings ** 2).sum(axis=1))[:, np.newaxis]
    return user_ratings @ user_ratings.T / (norm @ norm.T)


# 计算用户间的相似度
similarity_matrix = cosine_similarity(ratings)

'''
3.为指定用户推荐电影
'''


def recommend_movies(user_id, similarity_matrix, ratings, n_recommendations=1):
    '''
    为指定用户推荐电影
    :param user_id:
    :param similarity_matrix:
    :param ratings:
    :param n_recommendations:
    :return:
    '''

    # 获取目标用户的评分向量
    user_vector = ratings[user_id]

    # 排除用户自己
    other_users = np.arange(ratings.shape[0])
    other_users = other_users[other_users != user_id]

    # 找到最相似的用户
    most_similar_user = other_users[np.argmax(similarity_matrix[user_id, other_users])]

    # 获取该用户评分过的且目标用户未评分的电影
    recommend_movies = ratings[most_similar_user, :] > 0
    not_watched_by_user = user_vector == 0
    movie_to_recommend = recommend_movies & not_watched_by_user

    # 获取推荐电影的索引和评分
    recommend_movies_indices = np.where(movie_to_recommend)[0]
    recommend_movies_scores = ratings[most_similar_user, recommend_movies_indices]

    # 返回前n个推荐
    top_n_indices = np.argsort(-recommend_movies_scores)[:n_recommendations]
    return recommend_movies_indices[top_n_indices]


# 位用户‘Bob’推荐电影
bob_recommendations = recommend_movies(user_to_idx['Bob'], similarity_matrix, ratings)
print("Recommended movies for Bob:", [list(movie_to_idx.keys())[idx] for idx in bob_recommendations])
