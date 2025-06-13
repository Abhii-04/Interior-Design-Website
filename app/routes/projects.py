from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models.project import Project

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects/new', methods=['GET', 'POST'])
@login_required
def new_project():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        budget = request.form.get('budget')
        
        new_project = Project(
            title=title,
            description=description,
            budget=float(budget) if budget else None,
            user_id=current_user.id
        )
        
        db.session.add(new_project)
        db.session.commit()
        
        flash('Project created successfully!', 'success')
        return redirect(url_for('auth.profile'))
    
    return render_template('new_project.html')

@projects_bp.route('/projects/<int:project_id>')
@login_required
def view_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    # Ensure the current user owns this project
    if project.user_id != current_user.id:
        flash('You do not have permission to view this project', 'danger')
        return redirect(url_for('auth.profile'))
    
    return render_template('view_project.html', project=project)

@projects_bp.route('/projects/<int:project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    # Ensure the current user owns this project
    if project.user_id != current_user.id:
        flash('You do not have permission to edit this project', 'danger')
        return redirect(url_for('auth.profile'))
    
    if request.method == 'POST':
        project.title = request.form.get('title')
        project.description = request.form.get('description')
        budget = request.form.get('budget')
        project.budget = float(budget) if budget else None
        
        db.session.commit()
        
        flash('Project updated successfully!', 'success')
        return redirect(url_for('projects.view_project', project_id=project.id))
    
    return render_template('edit_project.html', project=project)