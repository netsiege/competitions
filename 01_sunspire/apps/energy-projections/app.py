from flask import Flask, request, render_template_string
import os
from dotenv import load_dotenv



app = Flask(__name__)
load_dotenv()
# Load config from environment
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-me')

TEMPLATE_BASE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sunspire Energy Projections</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a2e; color: #eee; }
        h1 { color: #f39c12; }
        .container { max-width: 800px; margin: 0 auto; }
        .card { background: #16213e; padding: 20px; margin: 20px 0; border-radius: 8px; }
        a { color: #3498db; }
        input, textarea { padding: 10px; margin: 5px 0; width: 300px; }
        button { padding: 10px 20px; background: #f39c12; border: none; cursor: pointer; }
        pre { background: #0f0f23; padding: 15px; overflow-x: auto; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sunspire Energy Projections</h1>
        <nav><a href="/">Home</a> | <a href="/forecast">Forecast</a> | <a href="/report">Custom Report</a></nav>
        <div class="card">
        %s
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    content = '''
        <h2>Welcome</h2>
        <p>Energy projection system for Sunspire grid management.</p>
        <ul>
            <li><a href="/forecast">View Forecast</a></li>
            <li><a href="/report">Generate Custom Report</a></li>
        </ul>
    '''
    return render_template_string(TEMPLATE_BASE % content)

@app.route('/forecast')
def forecast():
    content = '''
        <h2>7-Day Energy Forecast</h2>
        <pre>
Day 1: Solar 1,240 MW | Wind 890 MW | Demand 2,100 MW
Day 2: Solar 1,180 MW | Wind 920 MW | Demand 2,050 MW
Day 3: Solar 980 MW  | Wind 1,100 MW | Demand 2,200 MW
Day 4: Solar 1,320 MW | Wind 760 MW | Demand 1,980 MW
Day 5: Solar 1,290 MW | Wind 840 MW | Demand 2,150 MW
Day 6: Solar 1,100 MW | Wind 950 MW | Demand 2,080 MW
Day 7: Solar 1,350 MW | Wind 700 MW | Demand 1,920 MW
        </pre>
    '''
    return render_template_string(TEMPLATE_BASE % content)

@app.route('/report')
def report():
    # VULNERABILITY: SSTI - user input rendered directly
    template = request.args.get('template', '')
    
    if not template:
        content = '''
            <h2>Custom Report Generator</h2>
            <p>Generate a custom energy report using our template system.</p>
            <form method="GET">
                <textarea name="template" placeholder="Enter report template..."></textarea><br>
                <button type="submit">Generate</button>
            </form>
            <p><small>Example: Hello {{name}}</small></p>
        '''
        return render_template_string(TEMPLATE_BASE % content)
    
    # Vulnerable: renders user-supplied template
    try:
        result = render_template_string(template)
        content = f'''
            <h2>Generated Report</h2>
            <pre>{result}</pre>
            <a href="/report">Back</a>
        '''
    except Exception as e:
        content = f'''
            <h2>Error</h2>
            <pre>{str(e)}</pre>
            <a href="/report">Back</a>
        '''
    
    return render_template_string(TEMPLATE_BASE % content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
