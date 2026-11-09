
import http from 'k6/http';
import { check } from 'k6';

export const options = {
    vus: 1,
    duration: '10s',

    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};

export default function () {
    const resposta = http.get(
        'http://host.docker.internal:8000/livros'
    );

    check(resposta, {
        'status HTTP deve ser 200': (r) => r.status === 200,
    });
}
