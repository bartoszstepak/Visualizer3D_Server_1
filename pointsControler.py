from json import dumps
from points import Points
from flask import Flask, Response, request
from flask_cors import CORS
from math import *
import json


import helper


app = Flask('server')

CORS(app)

cors =  CORS(app, resources={
    r"/*": {
        "origins" : "*"
    }
})


@app.route('/', methods=['POST'])
def get_points():
    s = [
        [
            [0, 1],
            [1, 0]

        ],
        [
            [0, complex(0, -1)],
            [complex(0, 1), 0]

        ],
        [
            [1, 0],
            [0, -1]
        ]
    ]

    matrix = [
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]

        ],
        [
            [0, 1/2, 0],
            [1/2, 0, 0],
            [0, 0, 0]

        ],
        [
            [0, 0, 1/2],
            [0, 0, 0],
            [1/2, 0, 0]
        ]
    ]

    matrix220 = [
        [
            [-1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]

        ],
        [
            [0, 1, 0],
            [1, 0, complex(0, 1)],
            [0, complex(0, -1), 0]

        ],
        [
            [0, 0, 1 / 2],
            [0, 0, 0],
            [0, 0, 0]
        ]
    ]

    matrix2 = [
        [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0]
        ],
        [
            [0, 0, 0, 0, complex(0, -1)],
            [0, 0, 0, complex(0, -1), 0],
            [0, 0, complex(0, 1), 0, 0],
            [0, complex(0, 1), 0, 0, 0],
            [complex(0, 1), 0, 0, 0, 0]
        ],
        [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, -1, 0],
            [0, 0, 0, 0, -1]
        ]
    ]

    m62 = [
        [
            [1,0,0],
            [0,1,0],
            [0,0,-1]
        ],
        [
            [0,1/sqrt(2),0],
            [1/sqrt(2),0,1/sqrt(2)],
            [0,1/sqrt(2),0]
        ],
        [
            [0,complex(0, -1/sqrt(2)), 0],
            [complex(0, 1/sqrt(2)),0,complex(0, -1/sqrt(2))],
            [0,complex(0, 1/sqrt(2)),0]
        ]
    ]

    e64 = [
        [
            [0,1,0],
            [1,0,0],
            [0,0,-1]
        ],
        [
            [0,complex(0, 1/sqrt(2)), 1],
            [complex(0, -1/sqrt(2)), 0, 0],
            [1/sqrt(2), 0, 0]
        ],
        [
            [1 / sqrt(2), 0, 0],
            [0, 1 / sqrt(2), 0],
            [0, 0, -1 / sqrt(2)]
        ]
    ]

    e642 = [
        [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 0]

        ],
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]

        ],
        [
            [0, 0, complex(0, 1)],
            [0, 1, 0],
            [complex(0, -1), 0, 0]
        ]
    ]

    e66 = [
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0]

        ],
        [
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]

        ],
        [
            [0, 0, complex(0, 1 / sqrt(2))],
            [0, 0, 1/sqrt(2)],
            [complex(0, -1 / sqrt(2)) , 1 / sqrt(2), 0]
        ]
    ]

    e67 = [
        [
            [0, 0, 0],
            [0, 0, 1/2],
            [0, 1, 0]

        ],
        [
            [0, 0, 1/2],
            [0, 0, 0],
            [1/2, 0, 0]

        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
    ]
    reqMatrix = []
    reqDict = json.loads(request.data)
    m = reqDict.get("matricies")
    k = reqDict.get("k")
    n = reqDict.get("n")
    size = pow(n,2)

    # poprawić żeby był dobry format tablic
    m_test = helper.convert_request_matrix_to_numerical_matrix(m,k,n)

    # for i in range(k):
    #     reqMatrix.append([])
    #     matrix = m[i].get("matrix")
    #     for j in range(int(size)):
    #         reqMatrix[i].append(matrix[j].get("value"))

    points = Points(m_test, 2)
    generated_points = points.get_joint_numerical_range(10000)
    # qwe.qwe(generated_points)
    # qwe.qwe(helper.get_fibonacci_sphere_as_vectors(500))

    return Response(dumps(generated_points), mimetype='text/json')


def main():
    app.run(port=8870)


if __name__ == '__main__':
    main()