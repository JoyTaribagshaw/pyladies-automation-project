"""
Task Scheduler Demo

This module demonstrates how to schedule and run Python functions at specified intervals
using the schedule library. It includes examples of scheduling file organization,
email sending, and web scraping tasks.
"""

import time
import logging
import schedule
from datetime import datetime, timedelta
from typing import Callable, Dict, Any, Optional
from pathlib import Path

# Import our automation modules
from file_organizer import organize_downloads, clean_empty_directories
from email_sender import send_email

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('scheduler.log')
    ]
)
logger = logging.getLogger(__name__)

class TaskScheduler:
    """A class to manage and run scheduled tasks."""
    
    def __init__(self):
        """Initialize the task scheduler."""
        self.running = False
        self.jobs = {}
    
    def add_job(
        self,
        func: Callable,
        interval: str = 'daily',
        at: str = '09:00',
        args: tuple = (),
        kwargs: Optional[Dict[str, Any]] = None,
        job_name: Optional[str] = None
    ) -> str:
        """
        Add a job to the scheduler.
        
        Args:
            func: The function to schedule
            interval: 'minute', 'hourly', 'daily', 'weekly', 'monday', etc.
            at: Time to run the job (format: 'HH:MM')
            args: Positional arguments to pass to the function
            kwargs: Keyword arguments to pass to the function
            job_name: Optional name for the job
            
        Returns:
            str: Job ID
        """
        if kwargs is None:
            kwargs = {}
            
        job_name = job_name or f"job_{len(self.jobs) + 1}"
        
        # Schedule the job based on interval
        schedule_func = self._get_schedule_function(interval, at)
        if not schedule_func:
            raise ValueError(f"Invalid interval: {interval}")
        
        # Create the job
        job = schedule.every()
        schedule_func(job).do(self._run_job, func, job_name, *args, **kwargs)
        
        # Store job info
        self.jobs[job_name] = {
            'job': job,
            'func': func.__name__,
            'interval': interval,
            'next_run': job.next_run,
            'last_run': None,
            'last_result': None
        }
        
        logger.info(f"Added job '{job_name}' to run {interval} at {at}")
        return job_name
    
    def _get_schedule_function(self, interval: str, at: str = None):
        """Get the appropriate schedule function based on interval."""
        interval = interval.lower()
        
        if interval == 'minute':
            return lambda job: job.minute
        elif interval == 'hourly':
            return lambda job: job.hour
        elif interval == 'daily':
            return lambda job: job.at(at) if at else job.day
        elif interval == 'weekly':
            return lambda job: job.at(at).monday if at else job.monday
        elif interval in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            return lambda job: job.at(at).__getattribute__(interval) if at else job.__getattribute__(interval)
        else:
            try:
                # Try to parse as minutes
                minutes = int(interval.split()[0])
                return lambda job: job.minutes.until(minutes)
            except (ValueError, IndexError):
                return None
    
    def _run_job(self, func: Callable, job_name: str, *args, **kwargs) -> None:
        """Run a job and log the result."""
        logger.info(f"Running job: {job_name}")
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            status = "completed"
            logger.info(f"Job '{job_name}' completed successfully")
        except Exception as e:
            result = None
            status = f"failed: {str(e)}"
            logger.error(f"Job '{job_name}' failed: {e}", exc_info=True)
        
        # Update job info
        if job_name in self.jobs:
            self.jobs[job_name].update({
                'last_run': datetime.now(),
                'last_result': result,
                'status': status,
                'duration': time.time() - start_time
            })
    
    def run_pending(self) -> None:
        """Run all jobs that are scheduled to run."""
        schedule.run_pending()
    
    def run_all(self) -> None:
        """Run all jobs regardless of their schedule."""
        schedule.run_all()
    
    def start(self, interval: int = 60) -> None:
        """
        Start the scheduler.
        
        Args:
            interval: How often to check for pending jobs (in seconds)
        """
        if not self.jobs:
            logger.warning("No jobs scheduled. Add jobs before starting the scheduler.")
            return
        
        self.running = True
        logger.info(f"Starting scheduler with {len(self.jobs)} jobs")
        
        try:
            while self.running:
                self.run_pending()
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Scheduler stopped by user")
        except Exception as e:
            logger.error(f"Scheduler error: {e}", exc_info=True)
        finally:
            self.running = False
    
    def stop(self) -> None:
        """Stop the scheduler."""
        self.running = False
        logger.info("Scheduler stopped")
    
    def get_job_status(self, job_name: str) -> Optional[Dict[str, Any]]:
        """Get the status of a job."""
        return self.jobs.get(job_name)
    
    def get_all_jobs(self) -> Dict[str, Dict[str, Any]]:
        """Get all jobs and their status."""
        return self.jobs

# Example tasks
def organize_files_task():
    """Example task: Organize download folder."""
    print("\n=== Organizing Downloads Folder ===")
    organize_downloads()
    clean_empty_directories(str(Path.home() / 'Downloads'))
    print("Downloads folder organized!")

def send_daily_report():
    """Example task: Send a daily report email."""
    print("\n=== Sending Daily Report ===")
    send_email(
        to_email="your.email@example.com",
        subject=f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}",
        body="This is your automated daily report.\n\nHave a great day!"
    )
    print("Daily report sent!")

def backup_important_files():
    """Example task: Backup important files."""
    print("\n=== Backing Up Important Files ===")
    # This is a placeholder - in a real app, you would implement actual backup logic
    important_files = [
        str(Path.home() / 'Documents' / 'important.txt'),
        str(Path.home() / 'Documents' / 'projects')
    ]
    backup_dir = Path.home() / 'Backups' / f"backup_{datetime.now().strftime('%Y%m%d')}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Backing up {len(important_files)} items to {backup_dir}")
    # Actual backup implementation would go here
    print("Backup completed!")

def main():
    """Run the scheduler with example tasks."""
    print("=== Task Scheduler Demo ===\n")
    
    # Create a scheduler instance
    scheduler = TaskScheduler()
    
    # Add some example jobs
    try:
        # Run every minute (for demo purposes)
        scheduler.add_job(
            organize_files_task,
            interval='1',  # Every 1 minute
            job_name='organize_downloads',
        )
        
        # Run daily at 6:00 PM
        scheduler.add_job(
            send_daily_report,
            interval='daily',
            at='18:00',
            job_name='send_daily_report'
        )
        
        # Run every Monday at 2:00 AM
        scheduler.add_job(
            backup_important_files,
            interval='monday',
            at='02:00',
            job_name='weekly_backup'
        )
        
        # Print job list
        print("\n=== Scheduled Jobs ===")
        for job_name, job_info in scheduler.get_all_jobs().items():
            print(f"{job_name}: {job_info['interval']} at {job_info['job'].at if hasattr(job_info['job'], 'at') else 'now'}")
        
        # Start the scheduler (press Ctrl+C to stop)
        print("\nStarting scheduler. Press Ctrl+C to stop.")
        print("Jobs will run according to their schedule...\n")
        
        # For demo purposes, we'll run for a short time
        # In a real application, you might run this as a background service
        import time
        for _ in range(5):  # Run for 5 iterations (5 minutes in this demo)
            scheduler.run_pending()
            time.sleep(60)  # Check every minute
    
    except KeyboardInterrupt:
        print("\nScheduler stopped by user")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        print("\n=== Scheduler Summary ===")
        for job_name, job_info in scheduler.get_all_jobs().items():
            status = job_info.get('status', 'pending')
            last_run = job_info.get('last_run', 'Not run yet')
            print(f"{job_name}: {status} (last run: {last_run})")

if __name__ == "__main__":
    main()
