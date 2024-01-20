import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [data, setData] = useState([]);

    useEffect(() => {
        // Fetch data from your Django API endpoint
        axios.get('http://localhost:8000/api/stories/')
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Idea Database</h1>
            <ul>
                {data.map(story => (
                    <li key={story.id}>{story.title}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
